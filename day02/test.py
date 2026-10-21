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

# numbers = [1,2,3,4,5,6,7,8,9]

# for i in range(0 , len(numbers) // 2):
#     j = 2* i  +1
#     print(f"i = {i} , j = {j}")
#     numbers[j] = numbers[j] ** 2

# print(numbers)

# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}

# for number in numbers:
#     if number not in counter:
#         counter[number] = 0
#     counter[number]+=1

# print(counter)

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기" , "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is str or  type(character[key]) is int :
        print(f"{key} : {character.get(key)}")
    if type(character[key]) is dict :
           for value in character[key] :
                print(f"{value} : {character.get(key)[value]} ")
    if type(character[key]) is list :
            for value in character[key] :
                print(f"{key} :  {value}")


# 4- 3 -2
# key_list = ["name" , "hp" , "mp" , "level"]
# value_list = ["기사" , 200 , 30 , 5]
# character ={}

# for i in range(len(key_list)) :
#     character[key_list[i]] = value_list[i]

# print(character)


# 4 - 3 - 3
limit = 10000
i = 1
sum_value = 0
while sum_value < limit :
    sum_value +=  i
    i+=1
print("{}를 더할 때 {}을 넘으면 그때의 값은 {}입니다.".format(i-1 , limit , sum_value))


# 4- 3 -4 
# max_value = 0
# a = 0 
# b = 0 

# for i in range(1,100):
#     j = 100 - i
#     c = i * j
#     if  c >= max_value :
#         max_value = c
#         a = i
#         b = j
        
# print("최대가 되는 경우 : {} * {} = {}".format(a , b , max_value))