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


 