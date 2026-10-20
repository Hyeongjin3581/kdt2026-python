# p. 231 
# 범위 함수 : range( )
# 1. range( 끝값 ) , 시작갓 생략시  0부터
print( range(5) ) # range( 0 , 5 )
print( list( range( 5 ) ) ) # [0, 1, 2, 3, 4]

# 매개변수에 숫자 두 개 넣는 방법
# 2. range ( 시작값 , 끝값 )
print( list ( range ( 3 , 6 ) ) ) # [3, 4, 5]

# 3 . range( 시작값 , 끝값 , 단계 ) 
print( list ( range ( 0 , 10 , 2 ) ) ) # 0 부터 9 까지 2씩 증가.  /  [0, 2, 4, 6, 8]

# p. 233 
# for 과 range 함수 함께  , for 반복변수 in range( ) :
# 1] 1부터 10까지 출력
for i in range( 1, 11 ):
    print(i)

# 2] 
for i in range( 10 , -1  , -1 ):
    print( i )

# 3] 1부터 10까지 홀수만 출력
for i in range( 1, 11 , 2):
    print( i )

# 4] 구구단 : 단수 2부터 9까지  , 급수 1 부터커짐
for 단 in range( 2, 10 ,1):
    for 곱 in range(1 , 10 , 1):
        print(단 * 곱)


# p.240 
# while 조건식 :        # 조건이 True면 실행코드 반복실행, False 반복종료
#       실행코드 

i = 1
while i < 11 :
    print ( i )
    i += 1 # 파이썬 증감식연산자 x 

# 예 2] while 과 리스트
list_a = [ 1,2,1,2 ]
value = 2
while value in list_a :  # 찾을 값 in 리스트 내에 존재하면 True  , 반복실행. 
    list_a.remove( value )

print(list_a)  #  [1, 1]


# p.244 break , continue 키워드 : 반복문에서 사용하는 키워드 
for i in range(1 , 11 , 1):
    print(i)
    if i==3:
        break

for i in range( 1, 11 ,1):
    print(i)
    if i == 3:
        continue


pets = [
    {"name" : "구름" , "age": 5},
    {"name" : "초코" , "age": 3},
    {"name" : "아지" , "age": 1},
    {"name" : "호랑이" , "age": 1},
]

for i in pets:
    print(i["name"] , str(i["age"])+"살")
