# 예외객체란? 발생한 예외 정보를 갖는 객체
# 예외클래스 : Exception(예외 최상위클래스)
# except 예외클래스명 as 변수명 : 
# as 키워드 : 클래스의 객체변수 생성
# 그외 모든 예외 처리 : 여러개 except 에서 Exception은 항상 마지막에 위치
# 주의할점 : Exception 앞에 위치하면 아래 예외가 작동 안함. -> 상속 개념
# raise : 강제로 예외를 발생시킬 때 쓰이는 구문 

# p. 383
list_number = [52 ,273, 32 , 72 , 100]
try:
    number_input = int(input("정수 입력:"))  # 타입 예외
    print(list_number[number_input])            # 인덱스 예외 
    raise NotImplementedError # 아직 미구현 상태입니다. 를 뜻하는 구문
    #java : throws new 예외클래스( )
except ValueError as e :    # 타입변환 예외
    print( e )
except IndexError as e:     # 인덱스 예외
    print( e )
except Exception as e:      # 그 외(최상위) 예외 항상 마지막
    print( e )

# 게임 개발자들이 확인하는 예외처리는 경우의 수가 훠어어어어얼 ~ 씬 많음.
# 무튼 , 예외 처리시에 가장 중요한 것은 ' 이 코드에서 어떤 예외가 발생할 것인가? ' 를 잘 예측하는것이 중요하다.  