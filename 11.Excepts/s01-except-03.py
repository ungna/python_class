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

x = 10
y = 0

try:
    z = x / y # ZeroDivisionError: division by zero
except ZeroDivisionError as ex: # ex = ZeroDivisionError("division by zero")
    print("예외발생: ", ex)

# NameError: name 'z' is not defined
# print("z=", z)
   
try:
    print("x=", x)    
    print("y=", y)    
    print("z=", z)
except NameError as ex:
    print("예외발생: ", ex)
    
print("THE END")    


