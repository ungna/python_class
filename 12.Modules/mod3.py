# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:08:24 2023

@author: Solero
"""

# 모듈: mod3.py
# 함수나 변수, 클래스를 모아 놓은 파이썬 파일

PI = 3.141592

# 클래스 : 
class Math: # 수학함수
    @staticmethod
    def circlearea(r): # 원의 넓이
        return PI * (r ** 2)

    def circlearea2(self, r): # 원의 넓이
        return PI * (r ** 2)


# 함수 : 더하기
def add(a, b):
    return a + b

# 함수 : 빼기
def sub(a, b):
    return a - b

print("[mod2.py] __name__ : ", __name__)

# 테스트용 코드
if __name__ == "__main__": # 독립적으로 실행
    a = 10
    b = 20
    print(f"add({a}, {b}) -> {add(a, b)}")
    print(f"sub({a}, {b}) -> {sub(a, b)}")
    
    print(f"원의넓이(반지름:{a}) -> {Math.circlearea(a)}")
    
    math = Math()
    print(f"원의넓이(반지름:{a}) -> {math.circlearea2(a)}")
    
    # 권고하지 않음 : 가능하지만?
    print(f"원의넓이(반지름:{a}) -> {Math.circlearea2(Math(), a)}")
    
