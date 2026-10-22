 
# 구문 오류 : 실행 전 오류 , 실행 자체 불가능
# 런타임 오류 : 실행 중 오류 , 예외 

# 예외 처리 : 예외를 해결하는 모든 것  if로 하는 예외처리, try로 하는 예외 처리 차이점.

# 조건문 또는 Try 처리
# 예외처리는 사용자의 경험에 의존할 수 밖에 없음.  즉 , 코드를 중간중간 실행하면서 발생할만한 예외 처리 내용을 사용자가 이해하고 사용해야 함. 

# 예1]  조건문 예외

input_a = input("정수입력: ")
# int() 정수로 변환 함수
# int(input_a) # ValueError : --> 정수 입력안할 시 오류발생. 
if input_a.isdigit() :  # 문자열.isdigit() : 문자열타입의 값이 숫자이면 true .
    int(input_a)
else:
    print("정수가 아닙니다.")

# 예2] try 예외
try : 
    int (input_a)  # 예외가 발생할 것 같은 코드
except:
    print("정수가 아닙니다.") # 예외가 발생했을 때 실행할 코드

# 예3] pass 키워드 , 예외 어떻게 처리할지 모르는 경우 일단 넘어가기
try:
    int(input_a)
except:
    pass

# 예4] else , 예외가 발생하지 않았을 경우
try:
    int(input_a)
except: # 예외가 발생했을 때 실행코드
    print("정수가 아닙니다.")
else: # 예외가 발생하지 않았을 때 실행코드
    print("정수가 맞습니다.")


# 예5] finally , 예외가 발생하든 발생하지 않든 무조건 실행
try:
    int(input_a)
except: # 예외가 발생했을 때 실행코드
    print("정수가 아닙니다.")
else: # 예외가 발생하지 않았을 때 실행코드
    print("정수가 맞습니다.")
finally: # 무조건 실행되는 코드 ,  주로 외부 연결 종료시 사용.
    print("프로그램을 종료합니다.")

# 예 6 ] finally 활용 예
try :     # open(파일명 , 옵션) 파일 불러오기 함수 # w 옵션 : 파일이 없으면 생성
    file = open("info.txt" , "w")
    예외.발생해라() # 일부러 예외 발생
    # try 에서 만약에 예외가 발생하면 발생한 코드 이후는 실행안됨. -> except 이동
    # file.close() # 파일.close() : 파일닫기
except : 
    print("예외가 발생했습니다.")
finally :
    file.close() # 파일.close() : 파일닫기
print(file.closed) # False


# 예외처리 조합 

# try + except 구문 조합
# try + except + else 구문 조합
# try + except + finally 구문 조합
# try + except + else + finally 구문 조합
# try + finally 구문 조합