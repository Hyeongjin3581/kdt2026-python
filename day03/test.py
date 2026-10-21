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

numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda X : X % 2 == 1, numbers)))
print()

print(" # 3 이상  , 7 미만 추출하기")
print(list(filter(lambda X : X > 3 and X < 7 , numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda X : X * X < 50 , numbers)))

