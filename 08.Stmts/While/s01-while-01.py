# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:54:26 2023

@author: Solero
"""

# 반복문 : while
# while문의 조건식이 참이면 해당 블럭을 반복 실행

i = 0
s = 0

# 무한반복
while True:
    i += 1
    s += i
    print(f"과정: i({i}) = 합({s})")

print(f"최종: i({i}) = 합({s})")
        

#%%

# 무한반복
# 조건: 10번 반복
i = 0
s = 0

while True:
    # 종료조건: i 값이 10보다 크거나 같으면 블록(while) 탈출
    if i >= 10: 
        break
    i += 1
    s += i
    print(f"과정: i({i}) = 합({s})")

print(f"최종: i({i}) = 합({s})")

#%%

# 무한반복
# 조건: 10번 반복
l = 10
i = 0
s = 0

while True:
    i += 1
    # 종료조건: i 값이 10보다 크거나 같으면 블록(while) 탈출
    if i > l: 
        break
    s += i
    print(f"과정: i({i}) = 합({s})")

print(f"최종: i({l}) = 합({s})")


