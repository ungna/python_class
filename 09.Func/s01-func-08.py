# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:20:33 2023

@author: Solero
"""

#%%
# 함수(Function)

# 파라미터(parameter), 인수(arguments)
# 리턴(return) 
def titlex(title, msg, end):
    result = title
    result += ":"
    result += msg
    result += end
    return result # 리턴값


#%%

# 순서를 무시하고 파라미터의 이름을 지정하여 함수를 호출
print(titlex(msg="파라미터이름지정", title="확인", end='.'))
print(titlex(msg="파라미터이름지정", end=";", title="확인"))

# 파라미터의 일부만 이름을 지정
# 앞에서부터 생략이 가능
print(titlex("확인", msg="파라미터이름지정", end=";"))
print(titlex("확인", end='.', msg="파라미터이름지정"))

#%%
# SyntaxError: positional argument follows keyword argument
# print(titlex(msg="파라미터이름지정", end=";", "확인"))
# print(titlex("확인", msg="파라미터이름지정", ";"))

#%%


