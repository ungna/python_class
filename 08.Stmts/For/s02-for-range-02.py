# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:25:11 2023

@author: Solero
"""

# [문제]
# for 문을 이용하여 구구단을 출력하라.
# 2단부터 9단까지.

for x in range(2,10):
    print(f"{x}단 : ", end='')
    for y in range(1,10):
        print(f"{x * y:2d}", end=' ')
    print()
    
#%%

# [문제] for문을 사용해서
# 9칸짜리 피라미드를 그려라.
"""
    *
   ***
  *****
 *******
*********
"""

#%%
for n in range(1,10,2):
    p = '*' * n
    print(f"{p:^9}")
    
#%%
m = 9
for n in range(1,10,2):
    x = (m - n) // 2 # 공백의 갯수
    print(f"x({x}) : ", end='')
    for y in range(x): # 공백 출력
        print(' ', end='')
    for y in range(n): # 별 출력
        print('*', end='')
    print()

#%%

m = 9
for n in range(1,10,2):
    x = (m - n) // 2 # 공백의 갯수
    sp = x * ' '
    st = n * '*'
    print(f"{sp}{st}")
    
    
