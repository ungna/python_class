# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:53:01 2023

@author: Solero
"""

# 예외처리
# 런타임 오류 처리
# 실행시간에 발생하는 오류 처리
# 런타임 오류가 발생하면 프로그램이 종료


#%%

lst = [1,3,5] # 0,1,2

# IndexError: list assignment index out of range
# lst[3] = 99

try:
    lst[3] = 99
except IndexError as ex:
    print("예외발생:", ex)    

print(lst)

