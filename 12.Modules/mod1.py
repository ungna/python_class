# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:08:24 2023

@author: Solero
"""

# 모듈: mod1.py
# 함수나 변수, 클래스를 모아 놓은 파이썬 파일
print("[begin mod1.py]")

PI = 3.141592

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 테스트용 코드
a = 10
b = 20
print(f"add({a}, {b}) -> {add(a, b)}")
print(f"sub({a}, {b}) -> {sub(a, b)}")
print("[end mod1.py]")
