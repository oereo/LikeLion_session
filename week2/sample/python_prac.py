# 파이썬 코드 실습


# 자료형(리스트, 튜플, 딕셔너리)

# 리스트(List): 순서o, 중복o, 수정o, 삭제o
# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [1, 10, 'apple', 'banana', 'orange']
e = [1, 10, ['apple', 'banana', 'orange']]

# 인덱싱: 인덱스를 이용해 리스트 안에서 특정한 값을 가져옴
print("인덱싱 실습: ", d[2], d[-1])

# 슬라이싱: 인덱스를 이용해 일부분을 잘라서 가져옴
print("슬라이싱 실습: ", d[:2])
print("슬라이싱 실습: ", d[2:])

# 추가, 수정, 삭제
# 추가: append, extend
a.append(3)
a.append([4, 5, 6])
print("a에 append: ", a)

a.extend([1, 2, 3])
print("a에 extend: ", a)

# 수정
print("변경 전 a: ", a)
a[1] = 1000
print("변경 후 a: ", a)


# 삭제: remove, pop, del (remove: value, pop: index -> return: 삭제된 값, del -> 삭제된 값을 return하지 않음)
print("remove 전 a: ",a)
a.remove(3) # 3이라는 value를 삭제
print("remove 후 a: ",a)

print("pop 전 a: ",a)
a.pop(3) # 3번 index의 value를 삭제
print("pop 후 a: ",a)

print("del 전 a: ",a)
del a[1] # 1번 index의 value를 삭제
print("del 후 a: ",a)

# +a
# 리스트 길이: len
# 정렬: sort
print("a의 길이: ", len(a))
a.sort()
print("After sorting: ", a)

print('----------------------------------------')

# 튜플(Tuple): 순서o, 중복o, 수정x, 삭제x 
# 값이 변경되는 것을 방지하기 위해 중요데이터를 관리할 때 사용
# 선언
a = ()
b = (1, ) # ,가 없으면 b = 1과 같은 연산
c = (1, 2, 3, 4)

print('----------------------------------------')

# 딕셔너리(Dictionary): 순서x, 중복x, 수정o, 삭제o
# Key(변함x), Value(변함o, 변함x)
# 선언
a = {'name': 'Kim', 'phone': '010-1234-5678'}
b = {0: 'Hello', 1: 'World'}
c = {'arr': [1, 2, 3, 4, 5]}


# 추가
a['school'] = 'Chung-Ang Univ'
print(a)

# keys, values, items, get(key&value 한쌍)
print(a.keys())
print(a.values())
print(a.items())

print('----------------------------------------')

# 조건문(if-else)
arr1 = [0, 3, 5, 2, 7]
if 0 in arr1:
    print("0")
if 10 not in arr1:
    print("!=10")
elif 4 not in arr1:
    print("!=4")

print('----------------------------------------')

# 반복문
# 기본 반복문: for, while
v1 = 1
while v1 < 11:
    print("v1:", v1)
    v1 += 1
print("---------")
for v2 in range(1, 10):
    print("v2:", v2)
print("---------")
names = ["Kim", "Oh", "Park"]
for name in names:
    print(name)
my_info = {"Namm": "Kim", "Age": "25", "City": "Bucheon"}

# 순서 있는 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip


# 기본 값은 키


# keys
for key in my_info:
    print(key)
for key in my_info.keys():
    print(key)

# values
for value in my_info.values():
    print(value)

# items
for item in my_info.items():
    print(item)


# enumerate: 반복 횟수


# break


print('----------------------------------------')

# 예외처리(try-except)



print('----------------------------------------')

# 함수
# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)



# 코드상에서 명시적으로 자료형이나 반환값 힌트를 주기


print('----------------------------------------')

# 모듈
# 함수나 변수 또는 클래스를 모아 놓은 파일

# 선언
# import 모듈이름
# from 모듈이름 import 모듈함수
from datetime import datetime
print(datetime.today())

import random
print(random.randint(1, 10))

from random import shuffle
arr = [1, 2, 3, 4, 5]
shuffle(arr)