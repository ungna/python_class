# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:12:32 2023

@author: Solero
"""

# 함수
# 함수 안에서 선언한 변수의 효력 범위
# 함수 안에서 선언한 변수는 함수 안에서만 유효

#%%

# 함수 밖에서 선언된 변수 : 전역변수(global variable)
x = 20

# 함수 안에서 선언된 변수 : 지역변수(local variable)
# 파리미터 x는 전역변수(x)가 전달한 값을 받은 지역변수(x)
# func(x)는 call by value(값을 전달)
def func(x): 
    b = 10
    x += b
    return x

#%%

y = func(x) # x가 가지고 있는 값 20을 함수 func(x)로 전달

print('x=', x) # 전역변수 값 20은 변함이 없다.
print('y=', y) # 함수가 전달한 리턴값은 30

#%%

# 함수 안에서 선언된 변수 b는 함수 밖에서 참조할 수 없다.
# NameError: name 'b' is not defined
# print('지역변수(b)', b)








