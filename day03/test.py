# 5 - 1 - 2
# def mul(*values):
#     sum = 1
#     for value in values:
#         sum *= value
#     return sum

# print(mul(5,7,9,10))


# 5 - 1 - 3
# def func(*values , vA, vB ):
#     pass
# func(1,2,3,4,5)

# 5 - 3 - 1 
# numbers = [1 ,2 , 3, 4 ,5, 6]

# print("::".join(map(str ,numbers)))

# 5 - 3 - 2

# numbers = list(range(1, 10 + 1))

# print("# 홀수만 추출하기")
# print(list(filter(lambda X : X % 2 == 1, numbers)))
# print()

# print(" # 3 이상  , 7 미만 추출하기")
# print(list(filter(lambda X : X > 3 and X < 7 , numbers)))
# print()

# print("# 제곱해서 50 미만 추출하기")
# print(list(filter(lambda X : X * X < 50 , numbers)))

# ***** 5 - 2 -1 ******
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10 
전체사람의수 = 100
memo ={}

def 문제(남은사람수 , 최소사람수):
    key = str([남은사람수, 최소사람수])
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0:
        return 1
    # **** 재귀처리 ****
    count = 0
    for i in range(최소사람수 , 앉힐수있는최대사람수+1):
        count +=문제(남은사람수-i , i)

    # 메모화 처리
    memo[key] = count
    return count