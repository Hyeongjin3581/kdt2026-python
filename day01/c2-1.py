# 85p. 타입 확인하기 , type( 자료 )
print( type("안녕하세요") )  # <class 'str'>
print( type(123) )          # <class 'int'>
print( type(1.23) )         # <class 'float'>
print( type(True) )         # <class 'bool'>
print( type(None) )         # <class 'NoneType'>
print( type( [ ] ) )         # <class 'list'>
print( type( { } ) )         # <class 'dict'>
print( type( ( ) ) )        # <class 'tuple'>


# 86p. 문자열 만들기
print(" ABC ") # 큰따옴표 감싼
print(' ABC ') # 작은 따옴표 감싼
print("""A
B
C""")   # """여러줄""" 감싼
print("A'b'c") #작은따옴표 출력
print('A"B"c') # 큰따옴표 출력
print("\"A\'B\nC\tD\\E") # 제어문자

# 93p. 문자열 분산
# 1. +연결연산자
print( "안녕" + "하세요" )
# 주의 할 점 : 문자열 + 숫자는 연결 불가능

print("1" + "2")
print(1+2) 

# 2. 반복 연산자
print("안녕" * 3) # 안녕안녕안녕

#3. 인덱싱 , 문자열은 배열 / 리스트 이므로 인덱스가 존재한다. 
# 인덱스란 ? 0부터 요소들이 저장된 순서번호 , **음수도 가능(자바랑 다른 점) **
print("안녕하세요"[0]) # 안
print("안녕하세요"[2])  # 하
print("안녕하세요"[3])  # 세
print("안녕하세요"[-1]) # 요 / 역순 인덱스
# print("안녕하세요"[5]) # 인덱스가 넘치면 오류

# 97p. 

#4. 슬라이싱 , 문자열 자르기 / 일부 추출 split 과 같은 . [1:4]
print("안녕하세요"[0:2]) # 안녕
print("안녕하세요"[3:4]) # 세
print("안녕하세요"[3:5]) # 세요 / 띄어쓰면 공백도 포함하니 조심. 
print("안녕하세요"[0: ])  # 0 ~ 끝까지 # 안녕하세요
print("안녕하세요"[:3]) # 안녕하


# 5. 문자열의 길이 , len(문자열)
print(len("안녕하세요"))    # 문자열의 길이를 알려줌. 5


