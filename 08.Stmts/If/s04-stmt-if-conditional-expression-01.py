# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:40:41 2023

@author: Solero
"""

# 조건부 연산자(conditional expression)
# 변수 = 참 if 조건 else 거짓

x = 10
y = 11
z = True if x >= y else False 

print(f"x({x})는 y({y})보다 큰가? {z}")

# java
# boolean z = (x >= y) ? true : false;

#%%

if x >= y:
    z = True
else:
    z = False
    
print(f"x({x})는 y({y})보다 큰가? {z}")
    