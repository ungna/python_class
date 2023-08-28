# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:20:33 2023

@author: Solero
"""

#%%
# 함수(Function)

# 파라미터(parameter), 인수(arguments)
# 리턴(return) 
def titlex(title, msg):
    result = title
    result += ":"
    result += msg
    return result # 리턴값


#%%

msg = 12345

print(titlex("확인", str(msg)))
print(titlex(str(msg), "확인"))





