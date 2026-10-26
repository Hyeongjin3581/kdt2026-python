# 상속이란 ? 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스 만드는 것
# ininstance (인스턴스 , 클래스명)
# 예1
class Student : 
    def __init__(self):
        pass
class Human :
    def __init__(self):
        pass
student = Student()
print( isinstance(student , Student)) # True
print( isinstance(student , Human)) # False

# 예2] c8-1.py  클래스 코드 복사
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
             return  "{} \t {} \t {}".format(self.name , self.get_sum() , self.get_average())
        # 특수한 이름의 메소드 # 보조기능 재정의(오버라이딩)
        def __str__(self):
             return  "{} \t {} \t {}".format(self.name , self.get_sum() , self.get_average())
        # 특수한 이름의 메소드, / 비교 메소드 # 1. 총합계 비교 함수 재정의
        def __eq__(self, value):  # 오버라이딩   같을 때 사용
             return self.get_sum() == value.get_sum()
        def __ne__(self, value): # 같지 않을 때 
             return self.get_sum() != value.get_sum()
        def __gt__(self, value): # 클 때  
             return self.get_sum() > value.get_sum()
        def __ge__(self, value): # 크거나 같을 때
             return self.get_sum() >= value.get_sum()
        def __lt__(self, value): # 작을 때
             return self.get_sum() < value.get_sum()
        def __le__(self, value): # 작거나 같을 때
             return self.get_sum() <= value.get_sum()

students = [
    Student2("최윤성" , 87 , 98 , 88 , 85),
    Student2("최윤성" , 87 , 98 , 88 , 85),
    Student2("최윤성" , 87 , 98 , 88 , 85)
]

# 특수한 이름의 메소드 호출: str(인스턴스) → __str__ 실행

# __str__을 재정의하지 않으면 <__main__.Student2 object at 0x...> 형태(클래스명 + 주소값)로 출력 (Java의 toString()과 같다.)
print( str(students[0] ) ) # __str__ 함수가 실행된다.  / 최윤성   358     89.5
print (students[0] == students[1])  # 주소값은 다른데 , # == 대신에 __eq__ 함수가 실행된다 .
# 원래 객체는 다른데 , 우리가 __eq__ 메소드에서 같다 기준을 총합계로 정의하였으므로 # True. 
print( students[0] != students[1]) 
# 원래 객체는 다른데 , 우리가 __ne__ 메소드에서 다르다 기준을 총합계로 정의 했으므로 # False