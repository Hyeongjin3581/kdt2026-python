import numpy as np

# 1] 병합 , vstack([배열1, 배열2]), hstack([배열1, 배열2])
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
z = np.vstack([x, y])
print(z)

z = np.hstack([x, y])
print(z)

# 2] 병합2 , concatenate((배열1, 배열2), )
z = np.concatenate((x, y), axis=0) # axis = 0 행, axis = 1 열
print(z)
z = np.concatenate((x, y), axis=1)
print(z)

# 3] 정렬
x = np.array([3, 1, 4, 2, 5])
print(np.sort(x))
print(np.sort(x)[:: -1])
print(x) # 원본은 변경 안됨
x.sort() # 배열.sort()
print(x) # 원본 자체 변경

# 4] 값 자체를 정렬하지 않고 배열을 정렬 위치 순번 반환
scores = np.array([60, 21, 34, 70, 89])
z = np.argsort(scores) # 오름차순 기준으로 정렬했을 때 각 위치순번 반환
print(z)

# 5] 필터링/조건식 , for 사용안함(장점) : 내부적으로 사용 but 공학/AI 라이브러리 => C언어
x = np.array([10, 20, 30 , 40, 50])
print(x>30) # [False False False True True]
print(x[x>30]) # 인덱싱 안에 조건식 사용한면 True인 요소 추출 # [40, 50]
y = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(y % 2 == 0)
print(y[y%2==0])


# 6] 삼항연산자 , np.where(조건, 참 , 거짓)
print(np.where(y % 2 == 0, y, "거짓"))
print(np.where(y % 2 == 0, 0, 1)) # 짝수이면 0, 홀수이면 1

# 7] 다수조건 , & | ~
# 조건이 2개 이상일 때 () 또는 변수로 구분
a = y%2==0
print(y[ a & (y%4==0) ]) # 짝수이면서 4배수
print(y[a | (y%4==0)]) # 짝수이거나 4배수
print( y[ ~a]) # 짝수가 아닌
# 주의할 점 :  C / JAVA에서 & 비트(0/1)연산자 , numpy에서는 &논리연산자
# 넘파이는 파이썬 에서 실행되는 구조 (중복에 따른 오버라이딩 제약) bool  

# x & y        ← ① 파이썬 인터프리터가 문법을 해석 (파이썬 규칙을 따름)
#    ↓
#  x.__and__(y) ← ② 연산자를 파이썬 메서드 호출로 바꿈 (오버라이딩 지점)
#    ↓
#  np.bitwise_and(x, y)
#    ↓
#  C 루프 실행  ← ③ 원소 하나하나 계산 (C, SIMD) → 여기서 속도가 나옴
