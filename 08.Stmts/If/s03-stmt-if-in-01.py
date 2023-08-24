# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:27:39 2023

@author: Solero
"""

"""
해당하는 자료형에 x값을 가지고 있는가?
x in 리스트
x in 튜플
x in 문자열
"""

a = [1,3,5,7,8]
#%%

x = 7

if x in a:
    print(f"리스트 {a}는 ({x})값을 가지고 있다.")
else:
    print(f"리스트 {a}는 ({x})값을 가지고 있지 않다.")

#%%

x = 10

if x in a:
    print(f"리스트 {a}는 ({x})값을 가지고 있다.")
else:
    print(f"리스트 {a}는 ({x})값을 가지고 있지 않다.")

#%%

# x in 튜플

a = (1,3,5,7,9)
x = 7

if x in a:
    print(f"튜플 {a}는 ({x})값을 가지고 있다.")
else:
    print(f"튜플 {a}는 ({x})값을 가지고 있지 않다.")

#%%

# x in 튜플

a = (1,3,5,7,9)
x = 7

if x in (1,3,5,7,8):
    print(f"튜플 {a}는 ({x})값을 가지고 있다.")
else:
    print(f"튜플 {a}는 ({x})값을 가지고 있지 않다.")
