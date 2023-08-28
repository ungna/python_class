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

print(titlex("시작", "환영합니다"))
print(titlex("실행", "출발하세요"))
print(titlex("종료", "수고했습니다"))

#%%

start = titlex("시작", "환영합니다")
run = titlex("실행", "출발하세요")
end = titlex("종료", "수고했습니다")

print(start)
print(run)
print(end)

#%%

# TypeError: can only concatenate str (not "int") to str
# print(titlex("확인", 12345))

#%%
# TypeError: unsupported operand type(s) for +=: 'int' and 'str'
# print(titlex(1234, "확인"))





