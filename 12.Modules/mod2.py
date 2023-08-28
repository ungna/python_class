# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:08:24 2023

@author: Solero
"""

# 모듈: mod2.py
# 함수나 변수, 클래스를 모아 놓은 파이썬 파일

PI = 3.141592

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("[mod2.py] __name__ : ", __name__)

# 테스트용 코드
if __name__ == "__main__": # 독립적으로 실행
    a = 10
    b = 20
    print(f"add({a}, {b}) -> {add(a, b)}")
    print(f"sub({a}, {b}) -> {sub(a, b)}")
