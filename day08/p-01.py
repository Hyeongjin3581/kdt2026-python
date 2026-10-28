# 판다스 : 데이터 조작 및 분석(표형태) 라이브러리
# 설치 : pip install pandas
# 호출 

import pandas as pd

print(pd.__version__)

# 1] 데이터프레임 : 2차원(표) , pd.DataFrame(리스트 / columns=['열이름' , '열이름'])
data_list = [
    [ 'ant' , 25 , 'seoul'] ,
    ['bee' , 30 , 'busan'] , 
    ['cat' , 35 , 'incheon'] ] # 2차원 리스트
x = pd.DataFrame(data_list)
print(x) # 행과열 => 표 형식
x = pd.DataFrame(data_list , columns=['name', 'age' , 'city'])
print(x)
# 2] 데이터프레임2 , pd.DataFrame( 딕셔너리 ) , 키 (열이름)
data_dict = { 
  'name' : ['ant','bee','cat'] , 
  'age' : [25,30,35] , 
  'city' : ['seoul','busan','incheon'] } # 딕셔너리

# 2]
df = pd.DataFrame(data_dict)
print(df)         

# 3] 컬럼 값 추출 , df[ '열이름' ] ,
ages = df['age'] # 나이 추출
print( ages ) #Series(1차원)
print(type(ages)) # <class 'pandas.Series'>
print(type(ages.values)) # <class ' numpy.ndarray'>


# 4] 데이터프리이3 : pd.DataFrame(자료 , columns= [ ] , index = [ ])
import numpy as np
data_np = np.array(data_list) # 넘파이 자료
df = pd.DataFrame(
    data_np,
    columns= ['name' , 'age' , 'city'],
    index=['A' , 'B', 'C'])
print( df )

#RPA 업무자동화 

# 5] 주요 속성
print( df.shape ) # 행/열 크기 # (3, 3)
print( df.columns ) # 컬럼 목록 Index(['name', 'age', 'city'], dtype='str'
print( df.index ) # 인덱스 목록 Index(['A', 'B', 'C'], dtype='str')
print( df.values ) # 값만 2차원 리스트로 추출
print( df.head( 2 ) ) # 상위 n개 만 반환
print( df.tail( 2 ) ) # 하위 n개 만 반환
df.info() # 컬럼이름 , 결측치 , 타입 확인

# 6] 인덱싱 , df.iloc[행인덱스, 열인덱스] / df.loc[ 행라벨 , 열라벨 ] 
print( df.iloc[ 1 ] )    # 1행
print( df.iloc[ 1 , 2 ] ) # busan
print( df.loc['B'] )     # 1행 = B행
print( df.loc['B' , 'city'] ) # B행 city열  # busan

# df.loc[ df['FinalScore'] >= 90 ,  'Grade' ]  =  'A+'
#       └──── 행: 조건 ────┘           └ 열 ┘      └ 새 값 ┘
#       "90점 이상인 행들의"      "Grade 열을"  "A+로 바꾼다"

# 7] 슬라이싱 , [시작인덱스:끝인덱스] , [ 행슬라이싱 , 열슬라이싱 ]
print( df.iloc[ 0:2 , 0: 1 ] )
print( df.loc[ 'A' : 'C' , 'name' : 'age'] )

# 8] 열 추가 , df[새로운열] = 새로운값 
df['score'] = [ 100 , 80 , 95 ]
print( df )

# 9] 값 수정 , df[수정할열] = 새로운값
df[ 'age' ] = [ 31, 52, 40 ]
print( df )
df.loc['B' , 'age'] = 70 #B행age열 
print( df )
df.iloc[0,0] = 'apple'
print( df )

# 10] 여러개 수정 
df.loc[ ['A','B'] , 'score' ] = [ 50 , 60 ]
print( df )

# 11] 필터링(조건)
print( df['score'] > 70 )
#A    False
#B    False
#C     True 
print( df[ df['score'] > 70 ] )
#  name  age     city  score
#C  cat   40  incheon     95
cont = df['age'] >= 40
print( df[ (df['score'] > 70) & cont ] )
print( df[ (df['score'] > 70) | cont ] )
# 필터링 이용하여 새로운 열**
df['passed'] = False
df.loc[ df['score'] > 70 , 'passed' ] = True 
print( df )

# 12] 컬럼명 변경 , df.rename(columns={'기존열이름': '새로운열이름'}) → 새 데이터프레임 반환
df_kr = df.rename(columns={'city': '도시', 'age': '나이'})
print(df_kr)
# 혹은 df.info() 로 반환 가능

# 13 ] 집계 df.describe()  , df['열이름'].통계함수()
print( df.describe() )
#              age      score
# count   3.000000   3.000000
# mean   47.000000  68.333333
# std    20.420578  23.629078
# min    31.000000  50.000000
# 25%    35.500000  55.000000
# 50%    40.000000  60.000000
# 75%    55.000000  77.500000
# max    70.000000  95.000000

print(df['age'].sum())
print(df['passed'].value_counts()) # 자료 빈도 수


# 14 ] 합치기 / 병합
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Score': [90, 80, 85]})
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Score': [75, 95, 88]})
# 세로 연결 pd.concat( [df1 , df1] , axis = 0 세로연결 1 가로연결 , ignore_index=True)
new_df = pd.concat([df1 , df2] , axis=0 , ignore_index=True)
print( new_df)
new_df = pd.concat( [df1 , df2] , axis=1)
print( new_df )

# 병합 : 교집합(공통 컬럼) , pd.merge(df1 , df2 , on= '공통컬럼명' , how=' inner / outer ') 
df_info = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})
df_score = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})
new_df = pd.merge(df_info , df_score , on= 'ID' , how='inner') # inner(교집합)  / DB 와 비슷한 느낌이라고 생각하면 됨. 
print(new_df)
#    ID Name  Score
# 0   2  Bee     88
# 1   3  Cat     92

new_df = pd.merge(df_info , df_score , on= 'ID' , how='outer') # outer(NaN / 없는 자료는 다음과 같이 반환. )
print(new_df) #  NaN : 정의가 없는 자료 # 숫자가 아니다.  
#    ID Name  Score
# 0   1  Ant    NaN
# 1   2  Bee   88.0
# 2   3  Cat   92.0
# 3   4  NaN   85.0

# 15] 정렬 , df.sort_values(by = '컬럼명' ,  ascending=True오름차순 / False 내림차순)
df = pd.DataFrame({
  'name': ['Ant', 'Bee', 'Cat', 'Dog'],
  'age': [27, 27, 22, 32],
  'score': [88, 95, 85, 90]
})
# 다중정렬은 [ ] 리스트 사용 , *age 기준으로 1차 정렬 후 동일한 age 끼리 score 기준으로 2차정렬
new_df = df.sort_values(by= ['age' , 'score'] , ascending=True)
print(new_df)
# 컬럼명도 정렬이 가능하다 . axis = 0햏 / 1열
new_df = df.sort_index(axis=1 , ascending= True)
print( new_df)