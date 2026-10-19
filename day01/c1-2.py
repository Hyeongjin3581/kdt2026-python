# 파이썬 파일 만들기
# 파일명 뒤에 확장자(.py) 만든다.

#파이썬 주석
# 
# // 안돼용

print("Hello Coding Python");
# shift + enter 한줄씩 / 문장 실행
# 파일 내 오른쪽 클릭 -> run python -> 전체 실행

# 70p.
import keyword
print(keyword.kwlist)

# 77p.

# 하나만 출력
print("하나만 출력합니다.")

# 여러 개 출력 , 주의할 점 : , 쉼표 기준으로 공백 자동포함
print("여러개", "출력합니다")
print( )    # 한줄 공백 , 제어문자 \n 

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

# 104 p.  숫자연산자 
print(5+7 , 5-7 , 5*7, 5/7) # 사칙연산자
print(3//2 , 3%2 , 3**2 ) # 몫 // , 나머지 %  , 제곱 **
print( 5 + 3 * 2) # 11
print((5+3) * 2) # 16
print( 2 + 2 - 2 * 2 / 2 * 2) # 0
print(2 - 2 + 2 / 2 * 2 + 2) # 4