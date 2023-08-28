# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:12:40 2023

@author: Solero
"""

# 파이썬 확장자 (py) 생략
# mod3.py
# import 모듈이름
# 사용 : 모듈이름.함수(), 모듈이름.변수

# 사용할 때 모듈이름 생략
# from 모듈이름 import 모듈함수, 클래스, 변수

# 해당 모듈에서 전체 임포트
# from mod3 import *

# 해당 모듈에서 선택적으로 임포트
from mod3 import add, sub, PI, Math

a = 100
b = 200

a1 = add(a, b)
b1 = sub(a, b)

print("PI : ", PI)
print(f"add({a}, {b}) -> {a1}")
print(f"sub({a}, {b}) -> {b1}")

print(f"원의넓이(반지름:{a}) -> {Math.circlearea(a)}")
