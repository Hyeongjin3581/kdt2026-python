# 1] 항을 추가하는 함수
from sklearn.preprocessing import PolynomialFeatures # 항을 추가해주는 라이브러리
poly = PolynomialFeatures()         # 객체 생성
poly.fit( [ [2] ] )                              #  특성(2) 규칙
print(poly.transform( [ [2] ] ) )       # [[1. 2. 4.]] # 기본절편,원래값,제곱값

# 2] 절편 제외
poly = PolynomialFeatures(include_bias=False)
poly.fit([[2]])
print(poly.transform([[2]]))    # [[2 ,4.]]
# 3] 특성 2개인 경우
poly = PolynomialFeatures(include_bias = False)
poly.fit([[2,  3]])                      # 입력 [[2, 3]]은 특성이 2개(a=2, b=3)인 샘플 1개
print(poly.transform([[2 ,3]])) # [[2. 3. 4. 6. 9.]]
# 입력:  [x, y]
# 출력:  [x,  y,  x²,  xy,  y²]

# *] 특성 3개인 경우
poly = PolynomialFeatures(include_bias=False)
poly.fit([[2,3,4]])
print(poly.transform([[2,3,4]])) # [[ 2.  3.  4.  4.  6.  8.  9. 12. 16.]] # 

# 입력: [x, y, z]
# 1차: x, y, z                  (3개)
# 2차: x², xy, xz, y², yz, z²   (6개)
# → 총 9개  [[2. 3. 4. 4. 6. 8. 9. 12. 16.]]

# 2] 다항 회귀 모델
print()
import pandas as pd
df = pd.read_csv('./day13/Fish.csv')
# 1) 특성과 타깃 구성
X = df[ ['Length2' , 'Height' , 'Width'] ] # 특성3개
Y = df['Weight'] # 타깃 1개

# 2) 훈련용/테스트용 분리 8 : 2
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split( X , Y, test_size=0.2 , random_state=42)
# 3) 과소적합 방지 하고자 다항 만들기 == PolynomialFeatures
poly = PolynomialFeatures(include_bias=False)
poly.fit(X_train) # 학습할 특성들을 규칙(제곱/곱셈) 찾기
print(poly.transform(X_train))

X_train_poly = poly.transform( X_train ) # 라이브러리 활용하여 값 대입.
X_test_poly = poly.transform( X_test )
print(X_train.shape)
print(X_test_poly.shape)

# 4) 모델 학습
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_poly , Y_train) # 항이 추가된 특성으로 학습

# 5) 결정 계수
from sklearn.metrics import r2_score
Y_pred = model.predict( X_test_poly) # 테스트용 다항 특성으로 예측
print( 'r2 : ' , r2_score(Y_test , Y_pred)) # 0.9719372415762594



# 3] 다항의 차수 늘리기 , degree = 10 , 10차수
poly = PolynomialFeatures(include_bias=False , degree=10)
poly.fit(X_train)
X_train_poly2 = poly.transform(X_train)
print(X_train_poly2.shape)  # 차수2 --> 차수10 증가에 따른 (127, 285)항으로 증가.
X_test_poly2 = poly.transform(X_test)
# 학습 후 결정계수 확인
model = LinearRegression()
model.fit(X_train_poly2 , Y_train ) # 
from sklearn.metrics import r2_score
Y_pred2 = model.predict( X_test_poly2) # 테스트용 다항 특성으로 예측
print( 'r2 : ' , r2_score(Y_test , Y_pred2)) # 0.07276663213888512
# *] 모델 구현에서 다양한 속성값( degree = N ) 들을 테스트하여 설계/구현 한다. 

# RMSE 구하기
from sklearn.metrics import root_mean_squared_error
rmse = root_mean_squared_error(Y_test, Y_pred)
print(f"RMSE : {rmse:.2f}") # 63.18