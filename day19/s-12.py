from lightgbm import LGBMRegressor, early_stopping
import numpy as np
import pandas as pd
url = 'https://raw.githubusercontent.com/rashida048/Datasets/master/USA_cars_datasets.csv'
df = pd.read_csv(url)

df = df[df['price'] > 0]
num_cols = ['year', 'mileage']  # 수치형 --> 트리 모델이라 스케일링 불필요
cat_cols = ['brand', 'model', 'title_status', 'color', 'state'] # 범주형
# ** 만약에 모델의 성능 향상을 위해서는 도메인 지식의 (계산식)특성 추가 좋다. *

# 범주형 자료들을 원핫인코딩이 아닌 판다스 'category' 타입 변경
# --> 원핫인코딩 없이 LightGBM 내장 범주형 처리 사용 (범주들을 최적으로 묶어서 분할)
for col in cat_cols:
    df[col] = df[col].astype('category')

X = df[num_cols + cat_cols]
Y = df['price']
from sklearn.model_selection import train_test_split, KFold
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 1) 튜닝 -> optuna
# optuna 설치 : pip install optuna shap
import optuna
optuna.logging.set_verbosity( optuna.logging.WARNING )

# 2) 목적함수 만들기 : 각 탐색 시도마다 교차검증 수행 후 평균 성능 반환,  * 콜백함수( trial )
def objective( trial ) :
    # 2-1 교차검증 KFold
    cv = KFold( n_splits=5 , shuffle=True, random_state= 42)
    cv_r2_scores = [ ]      # 각 폴드별 검증 점수 저장
    best_iterations = [ ]   # 각 폴드별 최적 트리 번호 저장
    for train_idx , val_idx in cv.split( X_train , Y_train ) :
        # K 번째 폴드의 훈련용 / 검증용 인덱스 반환
        # 훈련 데이터 세트 내부에서 훈련용 / 검증용 분할 수행 , K =5 , 5 개 폴드 , 각각 한번씩 검증용
        X_tr , X_val = X_train.iloc[ train_idx ] , X_train.iloc[ val_idx ]
        Y_tr , Y_val = Y_train.iloc[ train_idx ] , Y_train.iloc[ val_idx ]
        # k폴드에서 분할한 훈련용 모델 만들기
        # trial.suggest_XXX( '파라미터명' , 시작값 , 끝값 ) * 파라미터명은 실제 LightGBM 파라미터명과 동일하게 *
        model = LGBMRegressor(
            n_estimators=1000,
            learning_rate=trial.suggest_float( 'learning_rate' , 0.01 , 0.1 ),          # 학습률
            num_leaves=trial.suggest_int( 'num_leaves' , 10 , 30 ),                     # 최대 리프 노드 수
            max_depth=trial.suggest_int( 'max_depth' , 3 , 10 ),                        # 최대 깊이
            min_child_samples=trial.suggest_int( 'min_child_samples' , 10 , 50 ),       # 리프 노드 최소 샘플 수
            subsample=trial.suggest_float( 'subsample' , 0.6 , 1.0 ),                   # 행 샘플링 비율
            colsample_bytree=trial.suggest_float( 'colsample_bytree' , 0.6 , 1.0 ),     # 열 샘플링 비율
            subsample_freq=1 , verbose=-1 , random_state=42 , n_jobs=-1
            # class_weight 회귀모델이므로 생략
        )
        # 2-2 폴드별 훈련용 / 검증용 으로 학습 , 검증용으로 조기 종료
        model.fit(
            X_tr , Y_tr ,
            eval_X=X_val , eval_y=Y_val ,
            callbacks=[ early_stopping( stopping_rounds=50 , verbose=False ) ]
        )
        # 2-3 폴드별 검증 평가 r2 저장
        r2 = model.score( X_val , Y_val )
        cv_r2_scores.append( r2 )                         # K 폴드별 평가 점수 저장
        best_iterations.append( model.best_iteration_ )   # K 폴드별 최적 트리 번호 저장
    # K폴드만큼 최적의 트리 리스트에서 평균값으로 trial 속성에 저장
    trial.set_user_attr( 'best_n_estimators' , int( np.mean( best_iterations ) ) )
    return np.mean( cv_r2_scores ) # 검증 평가 평균 점수 반환

# 3) optuna.create_study()
# 현재 실습은 회귀모델이며 , r2 결정계수 평가지표 사용 --> 클수록 좋으므로 maximize
sampler = optuna.samplers.TPESampler( seed = 42 )
study = optuna.create_study( direction='maximize' , sampler = sampler )
# study.optimize( 목적함수 , n_trials= 반복수 )
study.optimize( objective , n_trials=20 ) # --> 반복 수 만큼 목적함수 실행

# 4) 최적 하이퍼파라미터 / 최적 트리 개수
print( '최적 하이퍼파라미터 : ' , study.best_params )
best_n_estimators = study.best_trial.user_attrs['best_n_estimators'] # 모델이 아닌 트리 개수(숫자)
print( '최적 트리 개수 : ' , best_n_estimators )
print( '교차검증 평균 r2 : ' , study.best_value )

# 5) 최적 파라미터로 최종 모델 학습
final_model = LGBMRegressor(
    random_state = 42 , verbose=-1 , n_jobs=-1 , subsample_freq=1 ,
    **study.best_params ,               # 최적 파라미터 포함 # ** 딕셔너리 전개연산자
    n_estimators = best_n_estimators
)
final_model.fit( X_train , Y_train )
print( 'train r2 : ' , final_model.score( X_train , Y_train ) )
print( 'test r2 : ' , final_model.score( X_test , Y_test ) )
print( final_model.feature_name_ )
print( final_model.feature_importances_ )

# 교차검증 평균 r2 :  0.6360339980453231
# train r2 :  0.802857081755726
# test r2 :  0.7225798246456876
# ['year', 'mileage', 'brand', 'model', 'title_status', 'color', 'state']
# [299 862 202 412  52 226 483]


# 7) joblib 저장 / 로드
import joblib
joblib.dump( final_model , './day19/gbm_model.pkl ') # 1)
# 다른 .py 파일 또는 메소드 가정
model = joblib.load( './day19/gbm_model.pkl ') # 다른  .py 파일 또는 메소드 가정

# 8 ) 예측
new_cars = pd.DataFrame([
    {'year': 2019, 'mileage': 25000, 'brand': 'ford',   'model': 'f-150',  'title_status': 'clean vehicle',     'color': 'white', 'state': 'texas'},
    {'year': 2014, 'mileage': 85000, 'brand': 'nissan', 'model': 'altima', 'title_status': 'salvage insurance', 'color': 'black', 'state': 'california'}
])
for col in cat_cols:
    new_cars[col] = new_cars[col].astype('category')
###
preds = model.predict(new_cars)
print( '서빙 모델 예측 (1번차량)가격 : '  , preds[0])
print( '서빙 모델 예측 (2번차량)가격 : '  , preds[1])

# 서빙 모델 예측 (1번차량)가격 :  27543.39702099404
# 서빙 모델 예측 (2번차량)가격 :  821.4808765766404