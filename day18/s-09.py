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
plt.show()


# 트리란 ? 전체적인 의사결정 분기 구조
# 노드란? 사각형 상자 하나하나를 의미하며 , 최상단 노드를 ROOT 노드
# 노드 내부 속성 해석 
# X[0] 또는 특성명 <= 값  , 분기 조건(T : 왼쪽 / F : 오른쪽)
# gini = 값          , 지니 불순도 (0에 가까울수록 순수 , 0.5 혼잡) , 불순도가 낮아질 때 까지 가지치기. 
# sample = 값     ,  해당 노드의 데이터 총 개수 
#  Values <= [ 개수 , 개수 ], 해당 노드에 도달한 특성 값으로 분류한 특성들의 개수

