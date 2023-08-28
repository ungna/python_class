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
    print("args:", type(args)) # tuple
    tot = 0
    for score in args:
        tot += score
    avg = tot / len(args)
    return tot, avg # 다중 값 리턴 : 총점, 평균

#%%

t, a = totalavg(70, 80, 90)
print(f"총점({t}), 평균({a})")

#%%

t, a = totalavg(70,80,90,100)
print(f"총점({t}), 평균({a})")

