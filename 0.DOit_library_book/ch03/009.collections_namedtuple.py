# 자료에 이름을 붙이려면?
# collections.namedtuple: tuple은 인덱스를 통해서만 접근이 가능하지만
# nemadtuple은 인덱스 뿐 아니라 키로도 데이터에 접근하게 하는 자료형이다
# https://docs.python.org/ko/3/library/collections.html

from collections import namedtuple

# 리스트에 튜플요소 3건
data = [
    ('홍길동', 23, '01011111111'),
    ('김철수', 31, '01022222222'),
    ('이영희', 29, '01033333333')        
]

# namedtuple 자료형 생성
# 자료형의 이름  = namedtuple('자료형의 이름', '속성1, 속성2, 속성3, ...')
Employee = namedtuple('Employee', 'name, age, cellphone')


# data에 namedtuple 자료형 적용
data = [Employee(emp[0], emp[1], emp[2]) for emp in data]

# _make를 사용해 더 쉽게 만들수있음
# data = [Employee._make(emp) for emp in data]

#%%
'''
data = [Employee(emp[0], emp[1], emp[2]) for emp in data]를 풀어서 보기

'''

data = [
    ('홍길동', 23, '01011111111'),
    ('김철수', 31, '01022222222'),
    ('이영희', 29, '01033333333')        
]

Employee = namedtuple('Employee', 'name, age, cellphone')

data2 = []
for emp in data:
    name, age, cellphone = emp
    data2.append(Employee(name, age, cellphone))

data = data2

#%%
# namedtuple 호출

emp = data[0]        # ('홍길동', 23, '01011111111')
print(emp.name)
print(emp.age)
print(emp.cellphone)

#%%
# namedtuple 호출

print(data[0])
print(data[2].name)
print(data[1].age)

#%%
# namedtuple도 값을 변경할 수 없음

# data[0].name = '홍길동2'
# AttributeError: can't set attribute

# 값을 변경하려면 _replace를 써야 바꿀 수 있음
new_emp = data[0]._replace(name='홍길동2')
print(new_emp)
# 단 해당 객체를 직접 변경하는게 아니라 값을 변경한 새로운 객체를 만드는거임
print(data)  # 여기에는 없음
