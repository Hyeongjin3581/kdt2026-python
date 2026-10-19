# p115. 변수 
pi = 3.14159265 # 변수명 = 값
r = 10  # 변수명 = 값
# r2    # 초기값 없으면 NameError
print(pi, r) # 변수를 참조
print( 2 * pi * r)  # 62.831853

# p116. 복합 대입 연산자
number = 100    # 100
number += 10    #110
number -= 10    #100
number *= 2     #200    
number /= 2     #100
number %= 3    #1.0
number **= 3    #1.0
print(number)
number = "안녕하세요"
number += "!"   # 안녕하세요!
number *=3  # 안녕하세요!안녕하세요!안녕하세요!
print(number)

#p. 118 입력함수  , 반환타입 : 문자열 str
# input("인사말을 입력하세요>")
number = input("숫자를 입력하세영>")     # 입력받은 값 변수에 저장
print(type(number))     # 123 -> str , 안녕 -> str
# 121p. 타입변환 , str -> int/float

number_int = int(number)
number_float = float(number)
print(type(number_int) , type(number_float))

number_str = str(number_int)
print(type(number_str)) # <class 'str'>
# 주의할 점 : "a3" --> 숫자타입 반환 안됨.

# 125p. 누적예제
raw_input = input("inch 입력>") # 1. 입력받아 변수에 저장    
inch = int (raw_input)               # 2. 연산 전에 str -> int 형으로 저장
cm = inch * 2.54                       # 3. 연산
print( cm )                               # 4. 출력

# p135. , "문자열".format(값)
string_a = "age:{}".format(10)
print(string_a) # age : 10
string_b = "{} {} {}".format(1, "안녕" , True)
print(string_b)
# 주의할점 : {} 개수와 값의 개수는 일치해야 한다.