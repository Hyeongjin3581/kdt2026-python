# 지도 학습 : X 특성(독립) 과 Y 타깃(종속) 모델에 학습 하여 예측 / 
# 비지도 학습 : X 특성(독립) 모델을 이용하여 거리/ 밀도 군집/ 클러스터 / 그룹 예측 , 최적K(SSE , 실루엣)


# 실습에 필요 코드
import pandas as pd
url = "https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv"
df = pd.read_csv(url, sep=';')

X = df[['studytime', 'absences', 'G1', 'G2', 'G3']] # 공부시간 , 결석일수 , 1학기 ~ 3학기 성적
# 타깃 / 종속 없다 . -> 비지도 학습이라서
from sklearn.model_selection import train_test_split # 학습 98% , 검증용 2% ( 중요도는 떨어짐. )
X_train, X_test = train_test_split(X, test_size=0.02, random_state=42)

# 1) 스케일링/단위표준화 .
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train) # fit + transform => fit_transform
X_test_scaled = ss.transform(X_test)
# 2) 군집 = 그룹만들기 = 클러스터 , k개의 군집을 찾는 k_means 모델 , k_means( n_clusters=k )
from sklearn.cluster import KMeans
model = KMeans( n_clusters=3 ) # 모델 생성 / 주의할 점 : 만약 , 최대 학생이 10명일 때 클러스타수가 10개이면?
model.fit( X_train_scaled )
train_labels = model.predict( X_train_scaled ) # 군집 추론
print( '앞에서 10명 그룹 확인 : ' , train_labels[ : 10]) # 앞에서 10명 그룹 확인 :  [1 2 2 1 2 0 2 0 1 0] # 0 또는 1또는 2집합으로 클러스터링 
print( '테스트 학생 : ' , model.predict( X_test_scaled )) # [0 1 2 0 0 1 1 0]

# 3) 시각화 : 특성 여러개이므로 2D 시각화 한계
import numpy as np
list_2  = [ [2 ,3] , [ 4, 5] ]
print( list_2[ : 1]) # [[2, 3]] # 리스트 [ 시작행 : 끝행 - 1 ] 
arr = np.array(list_2) # 리스트 [행 : 열] # 생략시 전체 -> 전체행에 첫번째 열
print(arr[: , 1])  #[3 5]

arr[:, 1]     # [3 5]       → shape (2,)   1차원
arr[:, 1:2]   # [[3] [5]]   → shape (2, 1) 2차원 ✅
arr[:, [1]]   # [[3] [5]]   → shape (2, 1) 2차원 ✅
arr[:, 1].reshape(-1, 1)    # [[3] [5]]  → 1차원을 2차원으로 바꾸기

import matplotlib.pyplot as plt
plt.scatter( X_train_scaled[ : , 4 ] ,X_train_scaled[: , 1] ,c=train_labels)
plt.scatter( X_test_scaled[ : , 4 ] ,X_test_scaled[: , 1] ,c="red" , marker="*")
plt.show()

# 4) 최적의 K(군집/그룹) 수 찾기 VS 지도학습( F1 분류 / R2회귀 )
from sklearn.metrics import silhouette_score
sse_list = []
sil_list = [] 
for k in range( 2, 20 ) : # range( 시작값 : 끝값-1 )
    k_temp = KMeans( n_clusters=k , random_state=42 ) # k반복마다 학습 모델 생성
    preds = k_temp.fit_predict( X_train_scaled ) # 모델 학습 / 추론을 동시에 , fit + predict 
    sse_list.append( k_temp.inertia_) # 군집 결과에 각 샘플과 중심점 거리 제곱의 합
    sil_list.append( silhouette_score( X_train_scaled , preds) ) # 실루엣 점수를 저장
plt.plot( range(2, 20) , sse_list , marker='o' )
plt.show()

plt.plot( range(2, 20) , sil_list , marker='o' )
plt.show()