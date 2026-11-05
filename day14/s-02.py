import pandas as pd
df = pd.read_csv('./day14/Fish.csv')
# 1. 특성 , 타깃 분류
X = df[ ['Length2'] ] # 2차원
Y = df['Weight'] # 1차원
# 2. 훈련용 / 테스트용 분리
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.2 , random_state=42)
# 3. 단순 회귀 모델
from sklearn.linear_model import LinearRegression
model = LinearRegression()
# 4. 학습
model.fit( X_train , Y_train )
# 5. 모델 결정계수
Y_pred = model.predict( X_test )
from sklearn.metrics import r2_score
r2 = r2_score( Y_test , Y_pred )
print("r2 : " , r2)  # 0.8199897860284712  --> 약 82%

# 1] 특성[x] 에 제곱하여 항 추가 . 
import numpy as np 
# np.column_stack( (배열1 , 배열2) ) <-- 배열 연결  
X_train_poly = np.column_stack( (X_train**2 , X_train) ) 
print( X_train_poly ) # [16.2] -> [ [ 262.44   16.2 ] ]
# 2] 제곱된 특성 모델로 학습
model = LinearRegression()
model.fit(X_train_poly , Y_train) 
# 3] 예측
print(model.predict([[30**2 , 30]])) # [405.27748848]

# 4] 시각화
import matplotlib.pyplot as plt
point = np.arange( 0 , 101 ) # 0 ~ 100 까지의 회귀선
point_poly = np.column_stack( (point**2, point) )# 특성과 동일하게 제곱항 추가

plt.scatter(X_train , Y_train) # 특성자료
# 회귀선
plt.plot(point , model.predict(point_poly) , color ="red")
plt.show()

# 5] 결정계수
X_test_poly = np.column_stack( (X_test**2 , X_test) ) # 테스트용도 제곱 
Y_pred = model.predict(X_test_poly)
print(r2_score(Y_test , Y_pred)) 
# 단순 선형 회귀 결정계수 : 0.8199897860284712
# 다항 선형 회귀 결정계수 : 0.8249869834428712

# 즉, 차수를 올리면 곡선을 표현할 수 있어 결정계수가 올라갈 수 있다.
# 단, 훈련 R²는 차수가 오를수록 계속 높아지지만,
#     테스트 R²는 최적 차수까지 오르다가 그 이후에는 과대적합으로 오히려 떨어진다.
# → 훈련/테스트 R²가 모두 높고 차이가 작은 차수가 최적 차수
