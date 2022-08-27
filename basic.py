# Python Stduy
# 다른 언어와 다른점, 특장점 위주로 공부해보자
# 당연히 해쉬가 주석
"""
멀티라인 주석
"""

# bool type -> 첫글자를 반드시 대문자로 써야한다
from ast import Lambda
import enum
from numbers import Number
import this


print(True)
print(False)

# Null -> 파썬에서는 None으로 표현
print(None)

# 나누기, 몫연산자
print(5/5) # 실수 리턴
print(5//5) # 정수 리턴

# 제곱 sqrt 안쓰네?
print(5**2)

#문자열 연산
print("1" + "2") # 합쳐짐.
# print("1" + 1) 이건 실패함
print("1" * 10) # 반복됨

#비교
print(5 > 0 and 10 > 5 or 4 ) # && 대신 and / || 대신 or VB 6.0하던 생각이 나는데?
print(not True) # ! 대신 not

# 멤버쉽 연산
print("A" in "ABC") # .contain 함수같은 행동을 한다
print("A" not in "BBBB") # 부정형은 in 앞에 not을 붙인다

# CAST
print(int("10") + int("20"))

# 조건문
## 괄호 없이 탭으로 구분하는게 인상적이다.
if 10 == 10:
    print("a")
elif 20 == 20:
    print("hi")
else:
    print("@")

## list
animals = ["00", 11] # 자료형이 달라도 상관없음

## access 
# animals[index]
print(animals[0])

# delete
print(animals[0])
del animals[0]
print(animals[0])
animals = [0, 11, 11, 11, 444, 555]
animals.pop()
print(animals,"----")
animals.pop(0) # by index
print(animals,"----")
animals.remove(11) # by value 인덱스가 낮은순으로 지워진다
print(animals,"----")

## append
# animals[1] = 3 <- 에러남
animals.append(11)
animals.append(22)
animals.append(33)

## slice
print(animals)
print(animals[1:3]) # start index :end index +1 따라서 1:1하면 암것도 안나온다
print(animals[-1]) # get last
print(animals[:]) # get all
print(animals[:3]) # 0 to 3

# len
print(len(animals))

# sort
animals.sort() # return none
print(animals)
animals.sort(reverse=True)
print(animals)

# get index by value
print(animals.index(11)) # 중복된경우 가장 먼저 검색된 값의 인덱스가 나온다
# print(animals.index(None)) 없는경우 ValueError발생

# tuple - 불변 list
# C# 등에서는 Pair같은 쌍형태를 Tuple타입이라고했는데 차이가 있는듯?
# api는 리스트와 같다
thisIsList = [1, "1"]
thisIsTuple = (1, "1")
alsoThisIsTuple = 1, "1"
print(type(thisIsList), type(thisIsTuple), type(alsoThisIsTuple))

# Cast List <-> Tuple
print(type(list(thisIsTuple)))
print(type(tuple(thisIsList)))

# dictionary - key / value data type
## php의 연관 배열이랑 흡사한듯, key간, value간 타입이 다르더라도 무방하다

dictionary = {
    "key": "value",
    0: 1
}

print(dictionary)

# unpacking
a, b, c = [1, 2, 3]
print(a,b,c)
a, b, c = (1, 2, 3)
print(a,b,c)
# for
# for 변수 in 시퀀스 자료형: 형태로 사용
# 시퀀스 자료형 Iterable 이랑 같은걸로 이해해도 괜찮은가??
# 시퀀스 자료형 - 리스트 / 문자열 / range class/ tuple / 딕셔너리
# 다른 언어들의 foreach같은 느낌이다

for i in animals:
    print(i)

for char in "this_is_lower_case":
    print(char.upper())

#range(start, end+1, step)
for i in range(1, 10): # 1 ~ 9 까지임
    print(i)

# list loop with index
for index, value in enumerate([1, 2, 3]):
    print(f"index {index} / value {value}")

# dictionary주의 사항 items()로 loop하지 않는다면 key만 가져오는 불상사가 나타난다
for i in dictionary.items():
    print(i) ## i[0] => key, i[1]=> value


# function
def test(val):
    return val

print(test(1))


## 아래처럼 typehint 가능. 어디까지나 힌팅이라 오류가 발생하지 않는다
## ??? 이건좀 신기한듯 IDE를 위한 기능으로 판단
def test(name: str) -> int:
    return "123"

print(test(123))


# lambda

print((lambda i: i+1)(100))

#순서 조심해야할듯
testing = lambda i: True if i > 100 else False

print(testing(101))