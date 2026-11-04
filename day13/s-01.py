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
feature = ['Length2']        # 특성 : Length2 (물고기의 대각선 cm)  # 사이킷런 모델 구조상 학습할 특성은
target = 'Weigth'               # 타깃 : Weight(물고기의 무게 g)

# 3) 독립변수 / 입력변수 / 특성변수   , x y 구조
X = df[feature] # 2차원
Y = [target] # 1차원

# 4) 데이터 분리 , 학습용/테스트용 나누기 , 학습과 평과/예측성능 자료 구분
from sklearn.model_selection import train_test_split
# 특성학습자료 , 특성테스트자료 , 타깃학습자료 , 타깃테스트자료 =  train_test_split(특성 , 타깃 , test_size=비율 , random_state=난수시드값)
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 42)
#훈련세트 : 모델에서 규칙을 찾는 자료
#테스트세트 : 모델 학습 후 모델 평가 / 예측성능 점수 / 지표

# 5) 단순 선형회귀 모델
from sklearn.linear_model import LinearRegression # 선형회귀