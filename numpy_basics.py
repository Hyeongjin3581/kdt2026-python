"""NumPy 배열의 주요 속성 / 특징 / 리스트 비교 예제"""
import sys
import timeit

import numpy as np


def title(text):
    print(f"\n{'=' * 60}\n{text}\n{'=' * 60}")


# ------------------------------------------------------------
# 0. 배열의 주요 속성
# ------------------------------------------------------------
title("0. 배열의 주요 속성 (shape, ndim, size, dtype, itemsize, nbytes, strides)")
a = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],
              [[13, 14, 15, 16],
               [17, 18, 19, 20],
               [21, 22, 23, 24]]], dtype=np.int32)
print("shape   :", a.shape)      # 각 축의 길이
print("ndim    :", a.ndim)       # 차원 수
print("size    :", a.size)       # 전체 원소 수
print("dtype   :", a.dtype)      # 원소 타입
print("itemsize:", a.itemsize)   # 원소 1개 바이트
print("nbytes  :", a.nbytes)     # 데이터 전체 바이트 = size * itemsize
print("strides :", a.strides)    # 각 축으로 한 칸 이동할 때 건너뛰는 바이트

# ------------------------------------------------------------
# 1. 다차원 배열 객체 (ndarray)
# ------------------------------------------------------------
title("1. 다차원 배열 객체 (ndarray) - 동일한 데이터 타입")
mixed = np.array([1, 2.5, 3])
print("int + float 섞으면 ->", mixed, mixed.dtype)       # 자동으로 float64로 통일
with_str = np.array([1, "a", 3.0])
print("숫자 + 문자열 섞으면 ->", with_str, with_str.dtype)  # 전부 문자열이 됨

print("zeros :\n", np.zeros((2, 3)))
print("ones  :\n", np.ones((2, 3), dtype=np.int8))
print("arange:", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 5))

# ------------------------------------------------------------
# 2. 빠른 벡터화 연산
# ------------------------------------------------------------
title("2. 빠른 벡터화 연산 - 반복문 없이 배열 전체에 연산")
prices = np.array([10000, 25000, 8000, 42000])
print("원가        :", prices)
print("10% 할인    :", prices * 0.9)
print("2만원 이상? :", prices >= 20000)
print("2만원 이상만:", prices[prices >= 20000])   # 불리언 인덱싱

# ------------------------------------------------------------
# 3. 배열 조작 기능 (reshape, 결합, 분리)
# ------------------------------------------------------------
title("3. 배열 조작 - reshape / 결합 / 분리")
x = np.arange(12)
print("원본 :", x)
m = x.reshape(3, 4)
print("reshape(3, 4):\n", m)
print("reshape(2, -1) -> shape", x.reshape(2, -1).shape)   # -1은 자동 계산
print("reshape는 복사 없이 같은 메모리를 공유?", np.shares_memory(x, m))
print("전치 m.T shape:", m.T.shape)

p = np.array([[1, 2], [3, 4]])
q = np.array([[5, 6], [7, 8]])
print("concatenate axis=0 (아래로):\n", np.concatenate([p, q], axis=0))
print("concatenate axis=1 (옆으로):\n", np.concatenate([p, q], axis=1))
left, right = np.split(m, 2, axis=1)
print("split -> left:\n", left, "\nright:\n", right)

# ------------------------------------------------------------
# 4. 수학 함수 지원 (통계, 선형대수)
# ------------------------------------------------------------
title("4. 수학 함수 - 통계 / 선형대수")
scores = np.array([[80, 90, 70],    # 학생 A: 국, 영, 수
                   [60, 85, 95],    # 학생 B
                   [75, 70, 88]])   # 학생 C
print("전체 평균        :", scores.mean())
print("과목별 평균 axis=0:", scores.mean(axis=0))
print("학생별 평균 axis=1:", scores.mean(axis=1).round(2))
print("과목별 표준편차   :", scores.std(axis=0).round(2))
print("최고점 위치 argmax:", scores.argmax(axis=1))

A = np.array([[2, 1], [1, 3]])
b = np.array([5, 10])
print("행렬곱 A @ A:\n", A @ A)
print("연립방정식 2x+y=5, x+3y=10 의 해:", np.linalg.solve(A, b))

# ------------------------------------------------------------
# 5. 브로드캐스팅
# ------------------------------------------------------------
title("5. 브로드캐스팅 - 크기가 다른 배열끼리 자동으로 맞춰 연산")
mat = np.arange(6).reshape(2, 3)          # (2, 3)
row = np.array([10, 20, 30])              # (3,)  -> (1, 3) -> (2, 3)
col = np.array([[100], [200]])            # (2, 1) -> (2, 3)
print("mat:\n", mat)
print("mat + 5 (스칼라):\n", mat + 5)
print("mat + row (3,):\n", mat + row)
print("mat + col (2,1):\n", mat + col)

# 실무 예: 과목별 평균을 빼서 '평균 대비 점수' 구하기 (3,3) - (3,)
print("과목 평균 대비 점수:\n", (scores - scores.mean(axis=0)).round(1))

try:
    mat + np.array([1, 2])                # (2,3) + (2,) -> 마지막 축 3 vs 2 불일치
except ValueError as e:
    print("브로드캐스팅 실패 예:", e)

# ------------------------------------------------------------
# 6. NumPy vs 파이썬 리스트
# ------------------------------------------------------------
title("6-1. 연산 방식 차이 (+ 연산자)")
lst = [1, 2, 3]
arr = np.array([1, 2, 3])
print("list + list :", lst + lst)        # 이어 붙이기
print("arr + arr   :", arr + arr)        # 원소별 덧셈
print("list * 2    :", lst * 2)          # 반복
print("arr * 2     :", arr * 2)          # 원소별 곱

title("6-2. 연산 성능 (원소 100만 개 제곱)")
N = 1_000_000
py_list = list(range(N))
np_arr = np.arange(N)
t_list = timeit.timeit(lambda: [v * v for v in py_list], number=10) / 10
t_np = timeit.timeit(lambda: np_arr * np_arr, number=10) / 10
print(f"list 컴프리헨션: {t_list * 1000:8.2f} ms")
print(f"NumPy 벡터화   : {t_np * 1000:8.2f} ms")
print(f"-> 약 {t_list / t_np:.0f}배 빠름")

title("6-3. 메모리 효율 (실수 100만 개)")
float_list = [float(i) for i in range(N)]
list_bytes = sys.getsizeof(float_list) + sum(sys.getsizeof(v) for v in float_list)
print(f"list (포인터 + float 객체): {list_bytes / 1e6:6.1f} MB")
for dt in (np.float64, np.float32, np.float16):
    print(f"ndarray {np.dtype(dt).name:8s}       : {np.zeros(N, dtype=dt).nbytes / 1e6:6.1f} MB")

title("6-4. 차원 지원 (2x3 행렬의 열 합계)")
nested = [[1, 2, 3], [4, 5, 6]]
col_sum_list = [sum(r[j] for r in nested) for j in range(len(nested[0]))]
print("list :", col_sum_list, " <- 이중 반복 필요")
print("numpy:", np.array(nested).sum(axis=0), " <- axis 한 줄")
ragged = [[1, 2, 3], [4, 5]]
print("list는 행 길이가 달라도 됨:", ragged)
try:
    np.array(ragged)
except ValueError as e:
    print("NumPy는 직사각형 모양만 허용:", type(e).__name__)
