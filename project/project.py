import pandas as pd
from sklearn.model_selection import GridSearchCV, KFold, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression, Ridge , Lasso
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler , OneHotEncoder
df = pd.read_csv("./project/apt_data.csv")
print(df.shape) # (9079, 6)


X = df[['dong' , 'area' , 'floor' , 'build_year' , 'contract_year']]
Y = df['price']

#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
#  - 재현성을 위해 random_state=42로 고정합니다.
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.2 , random_state=42 , )

# 범주형 데이터를 수치형으로 . 

num_features = ['area' , 'floor' , 'build_year' , 'contract_year']
cat_features = ['dong']

pp = ColumnTransformer(
    transformers=[
        # passthrough --> 아무것도 하지 말고 그대로 통과. 
        ('num' ,'passthrough', num_features), # 수치형 , StandardScaler() 는 다항형으로 변환 까지 하고 , 2차항까지 만든 후 사용. 
        ('cat' , OneHotEncoder(drop='first' , sparse_output=False  , handle_unknown='ignore'), cat_features)
    ] #  handle_unknown='ignore --> ValueError
)
pp.fit(X_train)
X_train_pp = pp.transform(X_train)
X_test_pp = pp.transform(X_test)

import warnings
warnings.filterwarnings('ignore', category=UserWarning)   # 처음보는 동 경고 숨기기

# --> 수치형으로 변환 후 , 그 다음에 다항형으로 변환 .

# poly = PolynomialFeatures(include_bias=False , degree=2) # 차수는 2차항. 
# poly.fit(X_train_pp)
# X_train_poly = poly.transform(X_train_pp)
# X_test_poly = poly.transform(X_test_pp)
# print(X_train_poly.shape)  
# print(X_test_poly.shape)  

# ss = StandardScaler()  
# ss.fit( X_train_poly )
# X_train_scaled = ss.transform(X_train_poly)
# X_test_scaled = ss.transform(X_test_poly)

# # 스케일링 완료 이후 알고리즘 선택 . 

# #  단순선형회귀
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train_scaled , Y_train)
# #  결정계쑤
# print( 'r2 : ' , model.score( X_train_scaled , Y_train))  #  r2 :  0.8800727138183575
# print( 'r2 : ' , model.score( X_test_scaled , Y_test))  # r2 :  0.8869692371398133


# # 릿지 
# from sklearn.linear_model import Ridge
# # 2) alpha(규제강도) : 값이 커질수록 가중치/기울기를 0에 가깝게 규제 : 완만
# # 반복하여 최적의 규제 강도 찾기
# alpha_list = [0.001 , 0.01 ,0.1 , 1 , 10 , 100]
# for alpha in alpha_list:
#     model = Ridge(alpha= alpha) # 강도 설정하여 릿지 모델 객체 생성
#     model.fit(X_train_scaled , Y_train) # 학습
#     # 훈련데이터 점수와 테스트용 점수 격차 적은 alpha 찾기
#     print( "------ 훈련용 학습 데이터 점수 VS 테스트용 학습 데이터 점수 ------")
#     print( "Train R2 : " , model.score( X_train_scaled , Y_train ) )
#     print( "Test R2 : " , model.score( X_test_scaled , Y_test ) )

# # Train R2 :  0.8771020943698309
# # Test R2 :  0.8868192793511525


# # 라쏘
# from sklearn.linear_model import Lasso
# lasso = Lasso( alpha=10) # 임의의 강도 지정 라쏘 모델 객체 생성
# lasso.fit(X_train_scaled , Y_train)
# print( lasso.score(X_train_scaled , Y_train)) # 0.8449461738234318
# print( lasso.score(X_test_scaled , Y_test)) # 0.8550760982134302


# 선형 모델 파이프라인 구축.  
from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ('pp', pp),                                      # 원핫
    ('poly', PolynomialFeatures(include_bias=False)),  # 다항 (degree 탐색)
    ('scaler', StandardScaler()),                    # 스케일링
    ('model', LinearRegression())                # 모델 (종류 탐색)
])

param_grid = [
    {'poly__degree' : [1 ,2, 3], 'model' : [LinearRegression()]},
    {'poly__degree' : [1 ,2, 3], 'model' : [Ridge(random_state=42)] , 'model__alpha' : [0.01,0.1,1,10,100]},
    {'poly__degree' : [1 ,2, 3], 'model' : [Lasso(max_iter=10000)], 'model__alpha' : [1, 10, 100]}
]

kf = KFold( n_splits=5, shuffle=True , random_state=42) 

grid = GridSearchCV(
    estimator=pipe,
    param_grid= param_grid,
    scoring='r2',
    cv=kf,
    n_jobs= -1
)
grid.fit(X_train , Y_train)

print(grid.best_params_) # 최적의 파라미터  {'model': LinearRegression(), 'poly__degree': 2}
print(grid.best_score_)  # 최적 후보의 5-폴드 평균 R²  , 0.8754683720564967

# 최적모델 테스트
best_model = grid.best_estimator_
from sklearn.metrics import r2_score
Y_pred = best_model.predict(X_test)
r2 = r2_score(Y_test, Y_pred)
print('r2 : ', r2)  # r2 :  0.8869692371398133

import joblib 
joblib.dump(best_model , './project/apt_model.pkl')
model = joblib.load('./project/apt_model.pkl')

# 법정동별 실제 거래 범위 (프론트 입력 제한용) , 데이터에 없는 값으로 예측하지 않도록
dong_ranges = df.groupby('dong').agg(
    count = ('price', 'size'),               # 거래 건수
    area_min = ('area', 'min'),              # 전용면적 최소 / 최대 (㎡)
    area_max = ('area', 'max'),
    floor_min = ('floor', 'min'),            # 층 최소 / 최대
    floor_max = ('floor', 'max'),
    build_min = ('build_year', 'min'),       # 건축년도 최소 / 최대 / 중앙값(기본값)
    build_max = ('build_year', 'max'),
    build_median = ('build_year', 'median')
)

# 성능 지표 저장 (+ 프론트 드롭다운용 법정동 목록 , 법정동별 범위)
joblib.dump({
    'r2' : r2,
    'dong_list' : sorted(df['dong'].unique().tolist()),
    'dong_ranges' : dong_ranges.to_dict(orient='index') # { '여의도동' : { 'count' : 711 , 'area_min' : 33.71 , ... } }
}, './project/apt_metrics.pkl')

# 불러온 모델로 샘플 예측 테스트
sample = pd.DataFrame({'dong' : ['여의도동'], 'area' : [84.0], 'floor' : [10], 'build_year' : [2000], 'contract_year' : [2026]})
print('예측 거래금액(만원) : ', model.predict(sample))