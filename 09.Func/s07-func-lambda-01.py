# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:04:16 2023

@author: Solero
"""
# 함수
# 람다(lambda)
# inline 함수, 익명함수
# 함수명 생력, return 생략
# 
# 장점:
# 함수정의가 없다.
# 일회성으로 간결한 처리를 할 때 유용    
# 함수형 프로그래밍 기법을 적용할 수 있다.

# 선언
# 함수변수 - lambda 매개변수, ... : 표현식

#%%
# 일반함수
def add(a, b):
    return a + b

x = 10
y = 20
print("일반함수: ", add(10,20))
print(f"일반함수: add({x}, {y}) -> {add(x, y)}")

#%%

# 람다함수
lambda_add = lambda a, b : a + b
print("람다함수: ", lambda_add(10,20))
print("람다함수: ", lambda_add(99,1))

#%%

# 1회성 처리
print("10 * 20 -> ", (lambda x, y : x * y)(10,20))
print("10 ** 3 -> ", (lambda x, y : x ** y)(10,3))



