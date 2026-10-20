#p.192
#리스트란? 대괄화[] 엥 자료를 쉼표로 구분하여 여러 자료들으르 저장.
#[요소 , 요소 , 요소] , 요소 = element
# 인덱스란?  리스트 내 요소들이 저장된 순서번호 , 0 번시작

# 
list_a = [237 , 32 , 103 , "문자열" , True, False] # 리스트 선언
print(list_a[ 2 ]) # 103
print(list_a[ 1:3 ]) # 1~2 까지.      32 , 103 출력
list_a[2] = 7 # 요소 값 수정/변경 ***
print(list_a[2]) # 7

# *** 파이썬에서는 인덱싱이 음수로 가능하다. 
print(list_a[-2]) # = True가 나옴. 

print(list_a[3][1]) # 자
# print(list_a[1][1]) # TypeError

list_1 = [1 , 2,  3] # 1차원
list_2 = [[1 , 2] , [3, 4] , [5 , 6]]   # 2차원
list_3 = [[[1, 2] , [3, 4] , [5, 6]]]   # 3차원
print(list_2[1][0]) # 3
# print(list_3[3][1]) # 오류

# p.196 
list_a = [1 , 2,  3]
list_b = [4 , 5,  6]
print(list_a + list_b)  # 리스트 두 개를 붙인다. (리스트 + 리스트 => 연결)
print(list_a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3] / 반복연산자로 , 반복된다. 
print( len(list_a))  # 현재 리스트의 길이를 표현. length와 동일. (3) --> 0,1,2 
list_aa = [[1] , [2] , [3]]   # 2차원
print(list_a + list_aa)  # [1, 2, 3, [1], [2], [3]]

# append() --> 요소 끝에 추가.                              / 리스트명.append(요소)
# insert() --> 요소 중 원하는 곳에 삽입.                /  리스트명.insert(위치, 요소)
# extend() --> 한번에 여러 개의 요소를 추가.       /  리스트명.extend([리스트])
list_a.append(4); print(list_a)
list_a.insert(0,5); print(list_a)

# 주의할 점 : 
list_c = [1 ,2]
list_c + [3]                # 방법 1 ] [1 , 2 , 3] 새로운리스트 생성,  list_c 변화 없다 . 
list_c.append(3)        # 방법 2 ] [1 , 2 , 3]  기존 리스트 유지 , list_c 변화 있다 .

#p.202 인덱스로 요소 제거하기 . del 키워드 , pop()
list_a  = [1 , 2 , 3 , 4 , 5]
del list_a[1]  
print(list_a)   # [1, 3, 4, 5] / 1번째 요소 제거됨. 

list_a.pop(2)
print(list_a)  # [1, 3, 5] / 2번째 요소 제거됨. 

del list_a[1 : ]  # 슬라이싱 가능 
print(list_a)  # [1] / 1 이후의 요소들 전부 제거. 

# 값으로 제거하기 : 리스트명.remove(값)
list_a.remove( 1 )  # (1) 값 삭제
print(list_a)  # [] / 깡통만 남음 ㅋㅋ


# 리스트명.clear()
list_a.clear()

# *** 리스트 슬라이싱 ***
# 리스트[ 시작인덱스 : 끝 인덱스 : 단계 ]

numbers = [1,2,3,4,5,6,7,8]
numbers[0:5:2]   # [1, 3, 5]

numbers = [1,2,3,4,5,6,7,8]
numbers[ :  : -1]  # [8, 7, 6, 5, 4, 3, 2, 1]

# p.205 정렬 , 리스트명.sort() , 리스트명.sort( reverse = True )
list_e  = [52 , 273, 103 , 32 , 275 , 1, 7 ]
list_e.sort()
print( list_e )   # [1, 7, 32, 52, 103, 273, 275]
list_e.reverse()
print( list_e )   # [275, 273, 103, 52, 32, 7, 1]
# 만일 자바였다면 2배정도의 코드를 작성했어야 할 것. python에서의 정렬은 보다 단순함을 알 수 있다. 


# p.206 내부확인 , 찾을 값 in 리스트
print( 52  in list_e ) # True
print( 51  in list_e ) # False
print( 52  not in list_e ) # False
print( 51  not in list_e ) # True

#p.207 for반복문
# for i in range() 가 기본적인 형식. 
# for 반복자 in 반복할 수 있는 것:
#   코드

#ex)
i = 0
for i in range(3):
    print("안뇽")
# for문은 세로로 출력됨. (자동 줄바꿈)

# p. 208 리스트와 반복문
array = [237 , 32 ,103 , 57 , 52]

for i in array:
    print(i)

# 다음과 같이 출력된다. 
# 237
# 32
# 103
# 57
# 52

# p.209 중첩 리스트와 중첩 반복문
list_of_list = [
    [1 ,2 ,3],
    [4, 5, 6, 7],
    [8, 9]
]
for items in list_of_list:
    print(items)

# 다음과 같이 출력된다. 
# [1, 2, 3]
# [4, 5, 6, 7]
# [8, 9]

for items in list_of_list:
    for item in list_of_list:
        print(items)

# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]
# [4, 5, 6, 7]
# [4, 5, 6, 7]
# [4, 5, 6, 7]
# [8, 9]
# [8, 9]
# [8, 9]


# p.210 전개 연산자

a = [1 ,2 ,3 ,4]
b = [*a , *a]
print(b) # [1, 2, 3, 4, 1, 2, 3, 4]

# 전개 연산자를 사용하면 , append()함수같이 리스트에 요소를 추가할 때 코드를 비파괴적으로 구현할 수 있음. 



