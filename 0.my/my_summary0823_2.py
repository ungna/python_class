"""
# 리스트 자료형
배열(array): 연속된 동일한 자료형의 모음
리스트(list): 연속된 여러 자료형읨 모음
변경가능: mutable
리스트명 = [요소1, 요소2, 요소3,....]
[]을 사용해서 만듬
"""


# 빈 리스트
a = []
print(a, type(a))   # class =list

l = list()
print(l, type(l))

#%% list
# 다양한 형태의 자료형 저장 가능
b = [1,3,5,7]
c = [0, 0.12, True, 'English', '한글']

print(b)
print(c)

#%% list
# 리스트 안에 리스트
e = [1, 2, ['Life', 'is']]
print(e)

#%% list_indexing
print(e[0])
print(e[1])
print(e[2])  # ['Life', 'is']
  
print(e[2][0])   # Life
print(e[2][1])   # is 


#%% list_indexing_2
print(e[-1]) # ['Life', 'is']
print(e[-1][0])  # Life
print(e[-1][1])  # is

_e = e[-1]
print(_e[0])   # Life
print(_e[1])  # is

#%% list_indexing_3
# [0, 1, 2, 3, 4, 5]  슬라이싱 할떄 주의점은 [시작:끝] 일때 끝은 포함 x

a = [1, 2, 3, 4, 5]
a[0:2]  # 0~1까지     # [1, 2]
a[2:]  # 2~끝 까지    # [3, 4, 5]
a[:3]  # 처음~ 2 까지 #  [1, 2, 3]
a[:]  # 전체         # [1, 2, 3, 4, 5]

#%% list_indexing_내용물 변경_id

print(e, id(e))
print(_e, id(_e))

# [1, 2, ['Life', 'is']] -> [1, 2, ['Go', 'on']]
_e[0] = 'Go'
_e[1] = 'on'

print(e, id(e))     # id가 바뀜
print(_e, id(_e))  # id가 안바뀜 

#%% list_indexing_내용물 변경_id_정리

# 리스트안의 리스트 요소를 새 내용으로 변경해도
# 기존 리스트의 id가 안바뀐다
# 하지만 바꾼 리스트안의 리스트id는 바뀐다

e[-1] = [10, 20, 30]
# e와 _e의 관계가 끊김


print(e, id(e))  # 얘의 id는 [1, 2, ['Go', 'on']]일때랑 그대로 
print(_e, id(_e))       # before(['Go', 'on'])
print(e[-1], id(e[-1]))  # after([10, 20, 30]): 얘 id는 바뀜

e[1] = ['Go', 'on']
print(e, id(e))

e = e + [2,4,6]
print(e, id(e))  # 얘 id는 달라짐

#%% list_연산
## 더하기
# 사칙연산이 아니라 리스트에 추가되는 
# + 를 사용하면 id가 달라짐
d = [1,3,5] + [2,4,6]
print(d)

# 같은 번호가 있어도 걍 추가됨
e = [1,3,5] + [1,2,3]
print(e)


#%% list_연산
## 곱하기

a = [1,3,5]
b = [2,4,6]
c = a * 2
print(c)

# 리스트 곱하기는 한쪽이 정수여야함 

# d = a * b
# TypeError: can't multiply sequence by non-int of type 'list'

# d = a * 2.5
# TypeError: can't multiply sequence by non-int of type 'float'
# float도 안됨

#%% list_length
# 리스트의 길이
a = [1,3,5]
a_len = len(a)
print(a_len)

b = [1, 2, 3, [10, 20, 30]]
b_len = len(b)
print(b_len)   # 4   # 리스트 안의 리스트는 하나로 취급함 like indexing


#%% list_delete

a = [1, 3, 5, 7]

del a[1]
print(a)

# 전체 삭제
del a[:]
print(len(a))

#%% list_append  vs  extend

# append
# list에 요소 하나 추가

a = [1, 3, 5, 7]
print('추가전', a, id(a))

a.append(9)
print('추가후', a, id(a))   # append를 써도 id가 같음

# 리스트를 추가할 수 도 있음
a.append([1,2])
print(a)

a.append('ping')
print(a)

# extend는 리스트만 넣을 수 있음
a.extend([1,2])
print('추가후', a, id(a))        # append를 써도 id가 같음

# 문자열을 집어넣으면은 하나하나 분리되서 들어가짐
a.extend('ping')   # 'p' 'i' 'n' 'g' 이렇게 들어감
print(a)
#%%
x = [1, 2, 3]
y = []

for e in x:
    y.append(e*3)

print(y)


def mul(x, z):
    y = []
    for e in x:
        y.append(e * z)
        print()
    return(y)

print(mul([1,2,3,4,5], 3))



#%% list_sort(), reverse()
# 이때 리턴값 없이 정렬만 해주는거라 print(a.sort()) 하면 none뜸

# 오름차순
a = [1, 2, 3] * 3
print(a)

a.sort()
print(a)

# 정렬x 뒤집음(끝부터 넣음)
b = [1,6,2,7,4,8,9]
b.reverse()
print(b)

# 내림차순하려면은 정렬하고 reverse하면됨
b.sort()
b.reverse()
print(b)

#%%  list_index
# 리스트 안에서 값을 찾고 그 위치를 리턴함

#    0 1 2 3 4 5 6
b = [1,6,2,7,4,8,9]
b.index(7)   # 3

# 리스트 안에 없는 값을 넣으면은 오류남
# b.index(5)
# ValueError: 5 is not in list

# 값이 여러개 있으면은 제일 앞에 있는거의 위치를 알려줌
c = [1, 2, 3, 4, 2]
c.index(2)

#%% remove vs pop

# remove: 없앰 (리턴값x)
# 리스트 안에서 제일 먼저 나오는 값을 지움

a = [1, 2, 3] * 3
a.remove(2)
print(a)

# pop: 끄집어냄(리턴o)
# 리스트의 위치값을 리턴하고 그 요소를 삭제함
c = [1, 2, 3, 4, 2]
c.pop(0)
print(c)

c.pop() # ()안에 값을 안넣으면은 제일 마지막 요소를 리턴함
print(c)

#%% list_insert
# insert(a, b)
# a 위치에 b를 삽입

#    0 1 2 3 4 5 6
b = [1,6,2,7,4,8,9]
b.insert(3, '가')
print(b)



#%% tuple
'''
## 튜플(Tuple)
불변: 추가, 변경, 삭제 할 수 없음
 장점:
   속도가 빠름
   공간 절약
특징:
   기본적으로 리스트와 똑같음
   딕셔너리 키로 활용
   함수의 인자
   ()를 사용해서 만듬
   요소가 하나일때 반드시 마지막에 콤마
'''
# 빈 튜플
# ()를 사용해서 만듬
t1 = ()
t2 = tuple()
print(t1, type(t1))
print(t2, type(t2))

#%%
# 요소가 하나일때 반드시 마지막에 콤마
t3 = (1,)
print(t3)

t4 = (1,2)
print(t4)

#%% tuble 삭제하려 할때

t1 = (1, 2, 'a', 'b')

del t1[0]
# TypeError: 'tuple' object doesn't support item deletion
# 에러뜨고 삭제가 안됨 
# 변경할때도 마찬가지


#%% dict
'''
# dict: 사전형
키와 값을 한 쌍으로 선언
{키:값, 키:값, ...}
특징:
    검색(탐색)속도가 빠름
    처리 용량을 많이 차지함
    순차 검색속도가 느림
    순서가 없음  -> 인덱싱이 안됨
    키는 변하지 않는 값을 사용해야됨 -> 리스트 사용x 튜플은 사용o   
    키는 unique해야함 -> 중복되는 키 설정 불가
    {}를 사용해서 만듬
'''

# 빈 딕셔너리 생성
dt = {}
print(dt, type(dt))

#%% dict_값찾기
dt = {
      "title" : "Doit! 점프 투 파이썬",
      "author" : "python",
      "content" : "book",
      (1,) : "튜플은 가능"
      #[1] : "리스트는 불가능"
      }

print(dt)

# 키를 이용해 값을 찾을 수 있음
# dict이름['키이름']
print(dt['title'])

# get을 이용해 값찾기
# 값이 바로 리턴됨
dt.get('title')
dt.get('tlqksusdk')  # 없는 키를 get하면은 오류가 안나오 none을 리턴함
# 뒤에 값을 넣어서 키가 없을때 none대신 나오게 할수있음
dt.get('tlqksusdk', "없어ㅄ아")  

#%% dict_추가 및 값변경

# 없는 키에 값을 넣으면 추가가됨
dt["name"] = "한준희"

# dict는 index가 없고 키 값으로 value를 변경할 수있음
# 이미 존재하는 키에 넣으면은 값을 변경할 수 있음
dt['title'] = "Don`t Doit!"
print(dt['title'])

print(dt)

#%% dict_요소삭제
# 키를 지우면은 값도 같이 없어짐
del dt["name"]
print(dt)

# 전체 삭제
dt.clear()
print(dt)

#%% dict_키, 값 리스트 만들기
dt = {
      "title" : "Doit! 점프 투 파이썬",
      "author" : "python",
      "content" : "book"
      }

# 키, 값 목록 뽑기
dt.keys()
dt.values()

# 뽑은 키 목록을 리스트로 만들기
dt_keys = list(dt.keys())
dt_values = list(dt.values())


# 키, 값 쌍으로 얻기
dt.items()

#%% dict_찾기

# 해당 키가 딕셔너리 안에 있는지 확인
# T F 로 나옴
'title' in dt

'tlqksusdk' in dt


#%% pop을 이용하여 list를 dict로 만들기

t1 = [1, 2, 3, 4, 5]       # 키 list
t2 = [11, 22, 33, 44, 55]  # 값 list

dict = {
        t1.pop() : t2.pop(),
        t1.pop() : t2.pop(),
        t1.pop() : t2.pop(),
        t1.pop() : t2.pop(),
        t1.pop() : t2.pop()
        }

print(dict)



#%% Set
'''
# Set: 집합
ex) 합집합, 교집합, 차집합
특징:
    중복을 허용하지 않음
    순서가 없다 -> 인덱싱이 안됨
    set()  또는  {}사용
'''

# 빈셋
# set() 또는 {}사용
s = set()
s1 = set("Hello")
print(s1)     # 중복을 허용하지 않아서 H e l o 만 들어감

weeks = {'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}
print(weeks)


#%% set_교집합 &

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s1 & s2

#%% set_합집합 |

s1 | s2

#%% set_차집합 -

s1 - s2

#%% set_값 추가
s1 = set([1,2,3,4,5,6])

# add- 값 1개추가
s1.add(7)
print(s1)

# update - 값 여러개 추가
s1.update([8,9,0])
print(s1)

#%% set_값 제거
# remove
s1 = set([1,2,3])
s1.remove(2)
print(s1)



