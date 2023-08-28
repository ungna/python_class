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

# 함수에서 전역변수를 수정하려면?
def func(a):
    global x   # 전역변수를 바꾸겠다는 선언
    a *= x
    x = a      # 전역변수의 값을 변경
    return a

#%%

y = func(x) # x가 가지고 있는 값 20을 함수 func(x)로 전달

print('x=', x) # 전역변수 x의 값이 y와 동일해짐
print('y=', y) # 함수가 전달한 리턴값은 400





