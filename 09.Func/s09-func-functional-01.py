# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:14:10 2023

@author: Solero
"""
# 함수형 프로그래밍(Functional Programming)

def score(name): # 외부함수
    print(f"[score] name({name})")

    def minmax(*args): # 내부함수
        min = args[0]
        max = args[0]
        
        for val in args:
            if val < min:
                min = val
            if val > max:
                max = val
                
        return name, min, max
    
    return minmax # 내부함수를 리턴

#%%
s1 = score("[중간시험]")
s2 = score("[기말시험]")

print("중간시험 점수(최소값, 최대값)", s1(100, 90, 60, 70, 80))
print("중간시험 점수(최소값, 최대값)", s1(10,20,30))

#%%
print("기말시험 점수(최소값, 최대값)", s2(88,99,77,66,55,44))

