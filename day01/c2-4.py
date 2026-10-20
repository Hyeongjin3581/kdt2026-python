# p135. , "문자열".format(값)
string_a = "age:{}".format(10)
print(string_a) # age : 10
string_b = "{} {} {}".format(1, "안녕" , True)
print(string_b)
# 주의할점 : {} 개수와 값의 개수는 일치해야 한다.

# p.137 ~ p.140 생략
# p.141 대소문자 변환
a = "Hello" 
print(a.upper()) # HELLO
print(a.lower()) # hello

# p.142 양쪽 여백/공백 제거
a = " hello python "
print(a.strip())     # hello python (크롤링 ,전처리 시 양쪽 여백 제거에 사용됨.)

# p.143 , is000 구성 확인 , 반환타입 , True / False
print("Hello".isalpha())  # 알파벳으로 구성되어 있는지 확인. 
print("Hello".isdigit())   # 문자열이 숫자로 인식될 수 있는지 확인


# p.144 , find() vs indexOf()
output_a = "안녕안녕하세요.".find("안녕")
print(output_a)

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

# p.145 , 찾을 값 in 문자열 , 없으면 False , 있으면 True
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

