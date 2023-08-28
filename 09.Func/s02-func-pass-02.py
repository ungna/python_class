# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:20:33 2023

@author: Solero
"""

#%%
# 함수(Function)

# 아무것도 처리하지 않는 함수
# API 틀만 만들어 놓고 향후에 기능구현 예정
# 일부 블록을 pass로 처리할 수 있다.
def nothing(title, msg, end):
    print(f"title({title}), msg({msg}), end({end})")
    if isinstance(title, str) == (not True): # False?
        pass # 통과


#%%

nothing('시작','작업시작','.')





