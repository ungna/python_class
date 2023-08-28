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

# 파라미터에 전역변수와 같은 이름이 선언되어 있어도 지역변수로 처리한다.
def func(x):
    x += x  # 지역변수 x
    return x

#%%

y = func(x) # x가 가지고 있는 값 20을 함수 func(x)로 전달

print('x=', x) # 전역변수 값 20은 변함이 없다.
print('y=', y) # 함수가 전달한 리턴값은 30





