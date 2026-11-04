# 사이킷런 ? 방대한 머신러닝 알고리즘 모델 제공 라이브러리
# pip install scikit-learn

# 머신러닝 목표 : 추론/예측 과정
# 특성 : 모델이 학습하는 자료 정보 , 타깃 : 모델이 궁극적으로 정답을 맞혀야 하는 정답 정보 / 대부분 2차원 배열의 데이터 구조를 요구한다 . 
# 따라서 1차원 배열 형태의 데이터가 있다면 , 데이터를 2차원 리스트 형태로 변환해야 한다 . 

# 지도학습 : 문제와 그 정답을 제공하면서 학습시키는 방법. (회귀 / 분류)
# 비지도 학습 : 정답도 주지않고 , 오직 문제만 제공하여 스스로 구조를 파악시키는 방법 ( 군집 / 텍스트마이닝(텍스트분석) )


### 지도학습 실습 ### 

# 회귀모델 
# 1] 단순 선형 회귀 
# 1) 판다스로 자료 불러오기
import pandas as pd 

df = pd.read_csv('./day13/Fish.csv')
df.info()

# 2) 모델 학습에 사용할 데이터 추출
feature = ['Length2']        # 특성 : Length2 (물고기의 대각선 cm)  
target = 'Weight'               # 타깃 : Weight(물고기의 무게 g)

# 3) 독립변수 / 입력변수 / 특성변수   , x y 구조
X = df[feature] # 2차원
Y = df[target] # 1차원

# 4) 데이터 분리 , 학습용/테스트용 나누기 , 학습과 평과/예측성능 자료 구분
from sklearn.model_selection import train_test_split
# 특성학습자료 , 특성테스트자료 , 타깃학습자료 , 타깃테스트자료 =  train_test_split(특성 , 타깃 , test_size=비율 , random_state=난수시드값)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
#훈련세트 : 모델에서 규칙을 찾는 자료
#테스트세트 : 모델 학습 후 모델 평가 / 예측성능 점수 / 지표

# 5) 단순 선형회귀 모델
from sklearn.linear_model import LinearRegression # 선형회귀
model = LinearRegression() # 파이썬에서 객체생성 방법 ,변수명 = 클래스명( )
# 6) 모델학습 , model.fit(특성자료 , 타깃자료)
model.fit(X_train , Y_train)
# 7) 모델 가중치(기울기(a값)) , model.coef_
print( model.coef_ )    #   [30.43452394]
# 8) 모델 편향(y절편) 확인
print( model.intercept_)  # -477.30634978973194

# 9) 학습한 모델의 예측 , 새로운 x값을 넣어서 y값 구하기 , model.predict( 2차원특성자료 )
print( model.predict( [ [30] ] ) ) # 만약에 물고기 길이가 30일때 무게 예측 / 2차원 배열이라 [ [] ] 로 사용.
# *) 단순회귀모델 : y = ax + b , [30.43452394]*[30] + [-477.30634978973194]

import matplotlib.pyplot as plt
plt.scatter(X_train , Y_train)  # 자료를 점 형식으로 표시
plt.scatter([30] , model.predict( [[30]]) , color="red") # 임의의 예측 점
plt.plot([0, 100] , model.predict( [[0] , [100]] ) ) # 회귀선 : 임의의 최솟값 / 최댓값
plt.show()

# 11) 문제점
# x, y 가 직선 관계이며 실 자료들은 꼭 비례 증가가 아닐 수 있다.
# 해결 : 다항 회귀로 확장하여 특성추가 한다 . 

# 12) 모델 평가 , 테스트용자료사용
Y_pred = model.predict( X_test) # 테스트용 특성 넣어서 테스트 예측 결과
# - 평균 제곱근 오차 계산
import numpy as np
from sklearn.metrics import mean_squared_error # 평균 오차( 정답지와 예측 )
rmse = np.sqrt( mean_squared_error(Y_test , Y_pred)) 
print("rmse:" , rmse)  # rmse: 160.01413830813442 --> 예측이 실제 무게와 평균적으로 약 160g 차이남. 
# 해석 : 모델이 실제 무게와 얼마나 틀렸는지 평균 오차

# - 결정계수(R SCORE)
from sklearn.metrics import r2_score # 결정계수
r2 = r2_score( Y_test , Y_pred ) # 정답지와 예측값
print("r2 : " , r2) # r2 :  0.8199897860284712  --> 약 82%