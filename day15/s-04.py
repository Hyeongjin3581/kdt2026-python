import pandas as pd
df = pd.read_csv("./day15/Fish.csv") # 1) 자료 수집
X = df[['Length2', 'Height', 'Width']]# 2) 예측 할 특성과 타깃(정답) 선정 / 구성
Y = df['Weight'] #2) 타깃(정답) 선정 / 구성
# 3) 훈련 / 테스트 분리 
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42)
# 4) 과소적합 방지 하고자 항 추가  PolynomialFeatures # 제곱 / 곱셈
from sklearn.preprocessing import  PolynomialFeatures
poly = PolynomialFeatures( degree=2 , include_bias= False ) # degree = 2 기본값 / include_bias=False -> 편향값 1 제외.
poly.fit( X_train )
X_train_poly = poly.transform(X_train) # --> 항 추가
X_test_poly = poly.transform(X_test) # --> 항 추가

# 5) 항 많아지면 항/특성 간에 단위 표준화 / 스케일링 / 10 , 100 , 1000 , 10000 으로 스케일링 필요
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train_poly)
X_train_scaled = ss.transform( X_train_poly )
X_test_scaled = ss.transform( X_test_poly )

# 6) 모델 선택 = 단순선형회귀 / 규제(릿지 / 라쏘) alpha(규제강도 측정.)(기울기) --> 기울기를 조절하며 최적의 조건을 찾음 .
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_scaled , Y_train)
# 7) 결정계쑤
print( 'r2 : ' , model.score( X_train_scaled , Y_train)) # r2 :  0.9833194466740021
print( 'r2 : ' , model.score( X_test_scaled , Y_test)) # r2 :  0.9719372415762589

# ========================== (4) ~ (6) 과정 묶음
from sklearn.pipeline import Pipeline
# pipe_model = Pipeline( [("식별자" , 클래스명())] ) # 파이썬 인스턴스 생성 , 변수 = 클래스명 ( 인자값 ) 
# [] 리스트 () 튜플
pipe_model = Pipeline( [
    ('poly' , PolynomialFeatures(degree=2 , include_bias=False)), # 4
    ('scaler' , StandardScaler() ),                                                      # 5
    ('regressor' , LinearRegression() )                                              # 6
    ] ) 

# 9) 파이프라인으로 학습 
pipe_model.fit(X_train , Y_train)
print( 'r2 : ' , pipe_model.score( X_train , Y_train)) # r2 :  0.9833194466740021
print( 'r2 : ' , pipe_model.score( X_test , Y_test)) # r2 :  0.9719372415762589

# 10) 최적 (성능좋은 / 오차적은 ) 의 파라미터 (매개변수 /대입값) 찾기