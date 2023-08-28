# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:20:33 2023

@author: Solero
"""

# 함수(Function)

#%%
# 함수정의
# 파라미터 : 콘솔에 출력할 문자열
# 리턴값: None
def printx(msg):
    print("printx() : ", end='')
    print(msg)

#%%
# 함수호출    
# TypeError: hello() missing 1 required
# positional argument: 'msg'
# hello()    

#%%

printx("안녕?")
printx("반갑습니다.")






