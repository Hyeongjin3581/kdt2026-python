# https://canva.link/hrqmuqwz1koni0m

import numpy as np # py -m pip install numpy

print(np.__version__)

x = np.array([1 , 2, 3, 4])
print(x)

y = np.array([[1, 2, 3], [4, 5, 6]])
print(y)
# 동적 (자동으로 타입 정해주는) 타입 느리다 . 넘파이 정적타입
x = np.array([ 1, True , "안녕"])
print(x)  # ['1' 'True' '안녕']

# 2] 0으로 채워진 배열로 초기화 , zeros((행개수 , 열개수)) , 전처리시 활용 
x = np.zeros((2,3))
print(x)

# 3] 1으로 채워진 배열로 초기화 
x = np.ones((2, 3))
print(x)

# 4] range 와 유사 / start , stop , step 구조,  끝 값은 포함 안됨 ( 약간 0  ~ 9까지 인 느낌)
x = np.arange(0 , 10 , 2)
print(x) # [0 2 4 6 8]

# 5] 시작과 끝 사이 개수만큼 균등분할
x = np.linspace(0 , 1, 5)
print(x) # [0.   0.25 0.5  0.75 1.  ]

# [2] 배열의 주요 속성

# 2-1] 배열이 몇 행 몇 열인지 파악
x = np.array([[1,2,3],[4,5,6]])
print(x.shape) # (2, 3)

# 2-2] 배열 요소들의 데이터 타입(정수형 or 실수형)
x = np.array([1.0, 2.0, 3.0])
print(x.dtype) # float64 --> 실수형

# 2-3] 배열에 포함된 전체 요소의 개수
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x.size) # 9

#2-4] 배열의 차원 수 구분 (Vector(1차원) , Matrix(2차원) , Tensor(3차원) )
x = np.array([1,2,3])
print(x.ndim)
y = np.array([ [ [1],[2] ], [[3] , [4]] ])
print(y.ndim)

# [3] 배열의 데이터 타입 , np.array(리스트 / 튜플 , dtype = np.타입명) / 추후 [123] 대신 CSV 파일 같은 거 받아올 예정
x = np.array([1 , 2 , 3] , dtype = np.int32)
print( x.dtype) # int32
x = np.array([1.0 , 2.0 , 3.0] , dtype=np.float64)
print(x.dtype) # float64
x = np. array([True, False, True] , dtype=np.bool_)
print(x.dtype) # bool

# 데이터 타입 변환 (이미 생성된 배열의 데이터를 강제로 변환.) 0버림
# np.bytes : 영문또는 일부특수문자(아스키코드) 1바이트 , 한글(UTF-8) 3바이트
x = np.array([1.5,2.3,3.7])  
y = x.astype(np.int32)
print(y) # [1 2 3]

# |S6 : S=bytes 문자열(1글자 1바이트), 6=가장 긴 문자열 기준 원소당 6바이트 고정(전체 6×3=18바이트), |=바이트 순서(엔디언) 무관
x = np.array(['apple' , 'banana' , 'cherry'] , dtype=np.bytes_)
print(x.dtype) # |S6

# * 타입을 지정하는 이유 :  *
#    1] 메모리 효율성/속도/정밀연산  
#    2] 텐서플로우/파이토치 라이브러리