import pandas as pd
fish = pd.read_csv("./day16/Fish.csv")
# 1) 다중 분류 실습하기 위한 특성 / 타깃(여러개 어종) 구분

X = fish.drop( columns= ['Species']) # 어동 제외한 모든 열
Y = fish['Species']     # 어종 열

# 2) 분리 / stratify=Y 정답지에 학습용과 테스트용 비율 유지 (분류 모델 권장)
from sklearn.model_selection import train_test_split 
X_train , X_test , Y_train , Y_test = train_test_split(X,Y , test_size=0.2 , random_state=42 , stratify=Y)

# 3) 다항 위한 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)

# 4) 로지스틱 회귀 = 이진분류 또는 다중분류 자동선택된다 .
from sklearn.linear_model import LogisticRegression
model = LogisticRegression
model.fit(X_train_scaled , Y_train)
