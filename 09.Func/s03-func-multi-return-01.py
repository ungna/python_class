# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:06:10 2023

@author: Solero
"""

# 함수
# 멀티값 리턴


#%%

# 국어, 영어, 수학의 총점을 구하는 함수를 정의하라
def total(kor, math, eng):
    return kor + math + eng


#%%

kor = 100
math = 90
eng = 80

tot = total(kor, math, eng)
print(f"kor({kor}), math({math}), eng({eng}) = 총점({tot})")


#%%

# 국어, 영어, 수학의 평균을 구하는 함수를 정의하라
def average(kor, math, eng):
    return (kor + math + eng) / 3

avg = average(kor, math, eng)
print(f"kor({kor}), math({math}), eng({eng}) = 평균({avg})")











