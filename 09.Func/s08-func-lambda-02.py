# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:25:55 2023

@author: Solero
"""

# 함수 : 람다

#%%

# 콜백(callback)
# 처리 루틴에게 처리해야할 함수를 전달하여 
# 처리한 결과를 리턴하는 형태

# words : 처리를 해야 할 데이터
# callback : 처리해야 할 로직이 있는 함수
def soundwonder(words, callback):
    for word in words:
        print(callback(word))

#%%
        
words = ['hi', 'good', 'oh', 'nice']        

# 콜백함수
# 처리해야 할 로직
# 첫 번째 문자를 대문자로 바꾸는 함수
def wonder(word):
    return word.capitalize() + '!'

print("[일반함수] 첫번째 문자를 대문자로")
soundwonder(words, wonder)

#%%
def upper(word):
    return word.upper() + '!'

print("[일반함수] 전체 문자를 대문자로")
soundwonder(words, upper)

#%%

print("[람다함수] 첫번째 문자를 대문자로")
soundwonder(words, lambda word : word.capitalize() + '!')

#%%
print("[일반함수] 전체 문자를 대문자로")
soundwonder(words, lambda w : w.upper() + '!')
