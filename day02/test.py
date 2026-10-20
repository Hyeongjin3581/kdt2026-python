# numbers = [273 , 103 , 5 , 32 , 65 , 9 , 72 , 800 , 99]

# for number in numbers:
#     if number % 2== 0:
#         print(f"{number} 는 짝수입니다.")
#     else:
#         print(f"{number} 는 홀수입니다.")

# for number1 in numbers:
#     if(number1/100) >=1:
#         print(number1, "는 3 자릿수입니다.")
#     elif(number1/10) >=1:
#         print(number1 , "는 2 자릿수입니다.")
#     else:
#         print(number1 , "는 1 자릿수입니다.")

# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]

# for number in numbers:
#     output[(number -1) % 3].append(number)

# print(output)

numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0 , len(numbers) // 2):
    j = 2* i  +1
    print(f"i = {i} , j = {j}")
    numbers[j] = numbers[j] ** 2

print(numbers)