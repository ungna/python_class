# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:06:10 2023

@author: Solero
"""

# 함수
# 멀티값 리턴


#%%

# 국어, 영어, 수학의 총점과 평균을 구하는 함수를 정의하라
# 파라미터를 가변인자로 받음
def totalavg(*args):
    kor, math, eng = args
    tot = kor + math + eng
    avg = tot / len(args)
    return tot, avg # 다중 값 리턴 : 총점, 평균


#%%

kor = 100
math = 90
eng = 80

a, b = totalavg(kor, math, eng)
print(f"kor({kor}), math({math}), eng({eng}) = 총점({a})")
print(f"kor({kor}), math({math}), eng({eng}) = 평균({b})")

#%%

ta = totalavg(kor, math, eng)
print("총점, 평균 :", ta, type(ta)) # tuple

tot, avg = ta # unpacking: tuple
print(f"kor({kor}), math({math}), eng({eng}) = 총점({tot})")
print(f"kor({kor}), math({math}), eng({eng}) = 평균({avg})")







