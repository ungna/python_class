# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:03:15 2023

@author: Solero
"""

# 함수
# 가변인자: dict
# 파라미터를 딕셔너리로 받음
#%%


# [문제] 지정하지 않은 임의의 인자를 받아서 처리
# 파라미터의 이름이 정해지지 않음
# 파라미터의 dict의 키와 값을 출력하라.
# 파라미터의 타입이 dict인지 체크하라.(호출 오류 발생)
def unnamed(**kwargs):
    print(f"[xyz] type({type(kwargs)}), {kwargs}")
    
    for kw in kwargs:       # dict의 키를 하나씩 꺼냄
        value = kwargs[kw]  # 키를 가지고 값을 얻음
        print(f"key={kw}, value={value}")

#%%

# 
# TypeError: unnamed() takes 0 positional arguments but 3 were given
# unnamed(10,20,30)

#%%

# 
unnamed(a=10, b=20, c=30, d=40)    

#%%
# 
unnamed(x=10, y=20, z=30)    




