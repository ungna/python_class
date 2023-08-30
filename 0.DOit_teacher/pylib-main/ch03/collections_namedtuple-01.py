# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:25:03 2023

@author: Solero
"""

# collections.namedtuple
# 튜플에 이름을 지정하여 접근

from collections import namedtuple

# 리스트에 튜플 요소를 3건 
data = [
    ('홍길동', 23, '01099990001'), 
    ('김철수', 31, '01099991002'), 
    ('이영희', 29, '01099992003'),
]

print(type(data))


#%%
# namedtuple(대표이름, 튜플요소이름, ...)
Employee = namedtuple('Employee', 'name, age, cellphone')
print(type(Employee))

#%%
data = [ Employee(emp[0], emp[1], emp[2]) for emp in data ]
print(type(data))

# 위의 코드와 동일한 기능
"""
data2 = []
for emp in data:
    name, age, cellphone = emp
    data2.append(Employee(name, age, cellphone))
    
data = data2    
print("data2:", data2)    
"""

#%%
emp = data[0]           # 첫번째 직원
print('emp:', type(emp))
print(emp.name)         # "홍길동" 출력
print(emp.age)          # 23 출력
print(emp.cellphone)    # 01099990001 출력

#%%

print("# 전체 목록 출력 #")
for emp in data:
    print('name:', emp.name)
    print('age:', emp.age) 
    print('cellphone:', emp.cellphone)

#%%
print("# 전체 목록 출력(이름이 지정되지 않은 방식) #")
for emp in data:
    name, age, cellphone = emp
    print('name:', name)
    print('age:', age) 
    print('cellphone:', cellphone)





