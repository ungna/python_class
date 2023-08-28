# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:20:33 2023

@author: Solero
"""

#%%
# 함수(Function)

# 파라미터(parameter), 인수(arguments)
# 리턴(return) 
# 파라미터가 문자열이 아니면 오류 메시지를 리턴
def titlex(title, msg):
    if isinstance(title, str) != True:
        return f"title({title})의 자료형이 문자열이 아닙니다."
    if isinstance(msg, str) != True:
        return f"msg({msg})의 자료형이 문자열이 아닙니다."
    
    result = title
    result += ":"
    result += msg
    return result # 리턴값


#%%

print(titlex("확인", 12345))





