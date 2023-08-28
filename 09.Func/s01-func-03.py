# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:20:33 2023

@author: Solero
"""

# 함수(Function)


# 함수정의(function definition)
# 파라미터 : 출력 메시지 갯수
# 리턴 : 없음
def printx(msg, cnt):
    print(f'printx("{msg}", {cnt})')
    for x in range(cnt):
        print(f"{msg}({x+1})")

#%%

# 함수호출    
printx('Hello, World.', 10)    


