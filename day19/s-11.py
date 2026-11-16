# 실습에 필요한 데이터셋
import pandas as pd
url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
df = pd.read_csv(url)
X = df[['alcohol', 'sugar', 'pH']]
Y = df['class']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

##  1) lightGBM : LGBMClassifier 분류모델 , LGBMRegressor 회귀모델
from lightgbm import LGBMClassifier # 0 레드 , 1 화이트 / 와인 종류 분류
model = LGBMClassifier(
    # 다양한 매개변수(파라미터 설정)
    n_estimators=1000 ,          # 1) 추정기(모델) 최대 개수 설정, 기본값 100 / 실무 500 ~ 3000 , 넉넉히 넣고 조기 종료(early_stopping)로 최적 지점 찾음
    learning_rate=0.05 ,         # 2)  학습률(각 트리의 축소 비율) , 기본값 0.1 / 실무 0.01 ~ 0.1 , 낮출수록 과적합 줄고 정밀해지나 n_estimators 함께 늘려야 함
    num_leaves=15 ,              # 3) 단일 트리의 최대 리프 노드 수 , 기본값 31 / 실무 15 ~ 200 
    max_depth=6 ,                 # 4) 트리의 최대 깊이 , 기본값 -1(무제한) / 실무 3 ~ 8 
    min_child_samples=20 ,   # 5) 리프 노드 최소 샘플 수 , 기본값 20 / 실무 10 ~ 200 
    subsample=0.8 ,               # 6) 매 반복마다 랜덤으로 80% 만 무작위 샘플링 , 기본값 1 / 실무 0.6 ~ 0.9 , 노이즈 암기 줄여 일반화 성능 향상
    subsample_freq=1 ,          # 7) 6과 같이 설정하되 매 트리마다 배깅을 활성화.  /   , 기본값 0(비활성화) , 0이면 subsample 설정해도 작동 안 하므로 반드시 1 이상
    colsample_bytree=0.8 ,     # 8) 매 학습마다 랜덤으로 전체 특성 중  80 % 만 무작위 선택학습 .  / 기본값 1 / 실무 0.6 ~ 0.9 , 특정 핵심 변수에만 과도하게 의존하는 현상 완화

    class_weight='balanced',   # 9) *분류모델* 에서 타깃/종속 변수에 대해 불균형보정 /완화  , 기본값 None , 데이터가 균등하면 생략(None)
    verbose=-1 ,                      # 10) 매 학습마다 로그 숨김

    random_state=42 ,            # 13) 재현성을 위한 난수 시드 고정
    n_jobs=-1                          # 14) 모든 CPU 코어 병렬 사용
)
from lightgbm import early_stopping
from sklearn.metrics import classification_report, f1_score
# 2) 모댈 학습 수행 , 
# eval_set = [ (X_test , Y_test) ] : 조기 종료 하기 위한 (성능) 검증용 데이터셋 포함
# ~ 만약에 여러번 학습 중에 손실함수 결과 오차/잔차가 최적이 되면 종료 모니터링
model.fit(X_train, Y_train ,
        eval_set = [ (X_test , Y_test) ] ,
        callbacks = [early_stopping(stopping_rounds=50 , verbose=False)]
)
# 3 ) 주요 속성 확인 
print( model.best_iteration_) # 최적의 트리 반복 수 / 번호
print( model.feature_name_) # 각 특성의 이름                #  ['alcohol', 'sugar', 'pH']
print( model.feature_importances_ ) # 각 특성의 중요도 # [ 579 2284 1447]

# 평가지표
Y_pred = model.predict(X_test)
print("Train Acc :", model.score(X_train, Y_train))
print("Test Acc  :", model.score(X_test, Y_test))
print( f1_score(Y_test , Y_pred , average='macro'))  

# Train Acc : 0.8845487781412353
# Test Acc  : 0.8523076923076923   # 학습 - 테스트 => 0.03 => 3% (10% 아래로 과적합 억제)
# 0.8192436040044494

# 5) 예측하기 
new_wine = pd.DataFrame([
    [11.5 , 2.3 , 3.1] , [13.8 , 11.2 , 3.3]
])
new_pred= model.predict( new_wine )
print('예측1 : ' , new_pred[0]) #  0.0 : 레드 (당도 2.3 낮음)
print('예측2 : ' , new_pred[1]) #  1.0 : 화이트 (당도 11.2 높음)
# 알코올 / 당도 / 산도 를 비교했을 때 , 레드와 화이트 와인을 0 과 1로 나타냄