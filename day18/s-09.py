# 의사결정 결정트리
import pandas as pd

url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
df = pd.read_csv(url)
# alcohol,suger,pH,class(0:레드 / 1: 화이트)
X = df[['alcohol','sugar','pH']] # 독립변수
Y = df['class']

from sklearn.model_selection import GridSearchCV, KFold, train_test_split
X_train,X_test,Y_train,Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42, stratify=Y) # 분할

# 1) 결정트리 모델
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
# 종속/타깃이 범주형이면 XXXXClassifier, 연속형이면 XXXXREgressor
# 와인의 종류 예측 => DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train ,Y_train)
print( "Train Acc : " , model.score(X_train , Y_train))
print( "Test Acc : " , model.score(X_test , Y_test))
# Train Acc :  0.9978833942659227
# Test Acc :  0.8684615384615385 # 훈련용과 테스트 데이터간의 점수 차이가 10% 이상이면 과적합 => 규제
# !!! : 스케일링 / 표준화 필요없다 -> 원본 그대로 비교하여 분류하기 때문. 

# 2) 시각화 
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
# 트리 모델 시각화 # plot_tree(트리모델) / max_depth = 시각화할 깊이  / 스케일링 필요 x
plot_tree( model , max_depth=1 , feature_names=[ 'alcohol' , 'sugar' , 'pH' ] )      
# plt.show()


# 트리란 ? 전체적인 의사결정 분기 구조
# 노드란? 사각형 상자 하나하나를 의미하며 , 최상단 노드를 ROOT 노드
# 노드 내부 속성 해석 
# X[0] 또는 특성명 <= 값  , 분기 조건(T : 왼쪽 / F : 오른쪽)
# gini = 값          , 지니 불순도 (0에 가까울수록 순수 , 0.5 혼잡) , 불순도가 낮아질 때 까지 가지치기. 
# sample = 값     ,  해당 노드의 데이터 총 개수 
#  Values <= [ 개수 , 개수 ], 해당 노드에 도달한 특성 값으로 분류한 특성들의 개수


# 3) 규제 : 가지치기 ( 루트 개수 제한 )
model = DecisionTreeClassifier(
    max_depth=3,  #트리의 최대 깊이를 3으로 제한하여 복잡도 낮추기
    min_samples_leaf=10, # 리프노트(마지막노드)
    criterion="gini",
    random_state=42,
)
model.fit(X_train , Y_train)
print( "Train Acc : " , model.score(X_train , Y_train))
print( "Test Acc : " , model.score(X_test , Y_test))
# Train Acc :  0.8456802001154512
# Test Acc :  0.8407692307692308

# 4) 타깃 / 종속 클래스의 불균형 (레드 / 화이트 와인 개수 / 비율 다르다)
model = DecisionTreeClassifier(
    max_depth=3 , min_samples_leaf=10 , criterion="gini",random_state=42,
    class_weight="balanced" # 클래스 빈도에 반비례하여 가중치를 자동 부여하여 불균형 보정
)
model.fit(X_train , Y_train)
print( "Train Acc : " , model.score(X_train , Y_train))
print( "Test Acc : " , model.score(X_test , Y_test))
# Train Acc :  0.787569751779873
# Test Acc :  0.7946153846153846
# 성능이 (5%) 떨어짐 #  과도한 규제 -> 과소적합

# 5) 특성 중요도 : .feature_importances_ 
print( model.feature_names_in_ )
print( model.feature_importances_ ) # 분류모델에서 예측에 기여한 특성의 중요도 수치
# ['alcohol' 'sugar' 'pH']
# [0.06047705 0.92312892 0.01639403] # suger 특성이 중요도 수치가 가장 크다


# 파이썬 --> 모델을 만드는 작업은 매우 쉬워짐 (라이브러리 fit 한 줄)
# 그렇다면 중요한 것은 : 해당 모델의 과소 / 과대 적합을 어떻게 확인하고 ,
#   어떤 규제 / 하이퍼파라미터 조정을 통해 성능(결정계수 , F1 등)을 끌어올렸는가.
#   예) Train / Test 점수 비교 --> 규제(alpha) , 다항 차수(degree) , 트리 깊이(max_depth)를
#       교차검증(KFold + GridSearchCV)으로 탐색

# 개발 쪽으로 가면 코드 설계(구조)가 매우 중요함.
# 모델 자체(알고리즘 , LLM)를 새로 만드는 것은 실무에서도 난이도가 매우 높음.
# 허나 활용은 이미 만들어진 모델(라이브러리 , LLM)을 가져다 쓰기 때문에 상대적으로 난이도가 낮음.

## 실무 : 정형(표) 데이터에서는 앙상블 , 특히 부스팅(XGBoost , LightGBM , CatBoost)을 가장 많이 사용 ##
# --> 단 , 선형 / 로지스틱 회귀도 계속 사용
#     1) 기준선(baseline) : 단순 모델로 기준 성능을 잡고 , 앙상블로 얼마나 개선됐는지 비교
#     2) 설명이 필요한 분야(금융 심사 , 의료 등) : 계수로 결과 이유를 설명할 수 있음
# --> 하이퍼파라미터 탐색 : 부스팅은 파라미터가 많아 GridSearchCV(모든 조합)는 느림
#     --> RandomizedSearchCV , Optuna 등을 주로 사용
#     --> 단 , "교차검증으로 최적 파라미터를 찾는다"는 원리는 GridSearchCV 와 동일

## 포트폴리오 : 모델 종류보다 "과정"이 평가됨 ##
# 1) 데이터 이해 / 전처리 : 필터링 기준 , 이상치 확인 및 처리 근거
# 2) 검증 : 교차검증 , Train / Test 비교로 과소 · 과대적합 판단
# 3) 모델 비교 : 기준선 모델 vs 앙상블 모델 성능 비교
# 4) 서비스 연결 : 모델 저장(joblib) --> API 서버(FastAPI) --> 화면(HTML / JS)

# 6) 앙상블 : 여러개의 개별 모델을 조합하여 단일 모델보다 더 뛰어난 머신러닝 기법
# 배깅 앙상블 : 랜덤 포레스트 (여러 트리모델을 병렬 처리하여 최적의 모델을 찾기)
from sklearn.ensemble import RandomForestClassifier # 분류
model = RandomForestClassifier(
    max_depth=3, # 트리의 최대깊이 제한(과적합 억제)
    class_weight="balanced", # 클래스 불균형 해소 (과적합 억제)
    n_estimators=100, # 생성한 결정 트리 개수 기본값 100 , 1000 ~ 3000
    max_features='sqrt',  # 제곱근 (각 노드에서 분할 시 특성의 최대 개수)/ 회귀는  log 사용.
    random_state=42,
    n_jobs=1 , # CPU 최대 사용
)

model.fit(X_train , Y_train)
print( "Train Acc : " , model.score(X_train , Y_train))
print( "Test Acc : " , model.score(X_test , Y_test))

# n_estimators=1000 일시
# Train Acc :  0.7910332884356359
# Test Acc :  0.78

# n_ estimators 가 100일시, 
# Train Acc :  0.7852607273426977
# Test Acc :  0.7738461538461539

# n_ estimators 가 10일시, 
# Train Acc :  0.817009813353858
# Test Acc :  0.8007692307692308

# max_features='sqrt' 사용하는 이유 :  분류에서 샘플을 사용할 자료들을 전체 사용하지 않는다.
# 랜덤으로 4중에 4에 제곱근 하여 2개만 사용  sqrt{4} = 2
# 즉 ] 전체 (숲) 보는 방식이 아닌 (나무) 로 각기 다른 샘플을 사용

print( model.feature_names_in_)
print( model.feature_importances_)

# ['alcohol' 'sugar' 'pH']
# [0.06047705 0.92312892 0.01639403]