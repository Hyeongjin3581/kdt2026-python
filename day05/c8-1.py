# 절차지향 프로그래밍 : 데이터를 순서대로 처리하고 하향식 순차 실행 흐름 (C)
# 객체지향 프로그래밍 : 객체들의 상호작용으로 프로그래밍 설계 (Java/Python/JS/등등)
# 관점지향 프로그래밍 : 공통되는 기능(로그/검증/로깅/보안/등)들을 분리하여 프로그래밍 설계  (Spring)
# 면접을 볼 시 해당 내용들에 대해서 확답을 할 수 있어야 함. 
# 추상화 : 핵심적인 개념 또는 기능 간추려 내는 것
# 객체 : 속성명과 속성값으로 표현 
# [리스트] , {딕셔너리} 객체이다. 

# 클래스 : 객체를 조금 더 효율적으로 생성하기 위해서 만들어진 구문
# 클래스 --> 추상화한 데이터들을 구조화 한 것(설계도)

# 객체 : 세상에 존재하는 모든 데이터들을 추상화 (실체x) --> 개념적 객체
# 인스턴스 : 추상화한것을 객체로 만든것 (실체  o )  --> 물리적 객체 (컴퓨터 안에 메모리화)
# 인스턴스화 : 컴퓨터내 객체 정보 저장 , JAVA : NEW 생성자() , PY : 생성자()
# 생성자 : 클래스 기반으로 인스턴스 만드는 함수  -> 인스턴스 초기화함수 
# 한 줄 정의 : 생성자는 new로 객체를 만들 때 딱 1번 호출되어, 만들어진 객체(인스턴스)의 멤버변수를 초기화하는 블록이다. (메소드처럼 생겼지만 메소드가 아니다)

# 1. 클래스 만들기
# class 클래스명 : 
class Student :
    pass
student = Student() # JAVA : new Student() , PY : Student()
student = [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student()
]

#2 . 생성자
class Student2 :
    # def __init__(self, 멤버변수1 , 멤버변수2 , 멤버변수3):
        # self.멤베변수1 = 멤버변수1 ;
        def __init__(self , name , korean , math , english , science):
            self.name = name
            self.korean = korean
            self.math = math
            self.english = english
            self.science = science
        #def 메소드 명 (self , 매개변수1) :
        def get_sum(self) :
             return self.korean + self.math + self.english + self.science
        def get_average (self) :
             return self.get_sum() / 4
        def to_string(self) :
             return  "{} \t {} \t {}".format(self.name , self.get_sum , self.get_average)

# 일반함수와 메소드 차이? 일반함수는 클래스밖에서 독립선언 / 메소드는 클래스안에서 선언
# 일반함수에서는 self 없고 메소드는 self 있다. 
def get_sum2() : 
     pass

# 생성자 이용한 인스턴스 생성 , py : 클래스명 (인수 , 인수 , 인수)
# Student2 s = new Student("유재석" , 10 , 20 , 30 , 40)
students = [
    Student2("최윤성" , 87 , 98 , 88 , 85),
    Student2("최윤성" , 87 , 98 , 88 , 85),
    Student2("최윤성" , 87 , 98 , 88 , 85),
    Student2("최윤성" , 87 , 98 , 88 , 85),
    Student2("최윤성" , 87 , 98 , 88 , 85),
    Student2("최윤성" , 87 , 98 , 88 , 85),
]
# 인스턴스내 멤버변수 호출
print( students[0].korean )