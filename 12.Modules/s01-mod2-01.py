# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:12:40 2023

@author: Solero
"""

# 파이썬 확장자 (py) 생략
# mod1.py
# import 모듈이름
# 사용 : 모듈이름.함수(), 모듈이름.변수

import mod2

a = 100
b = 200

a1 = mod2.add(a, b)
b1 = mod2.sub(a, b)

print("PI : ", mod2.PI)
print(f"add({a}, {b}) -> {a1}")
print(f"sub({a}, {b}) -> {b1}")