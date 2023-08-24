# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:51:29 2023

@author: Solero
"""

# 반복문: for
"""
for 변수 in 리스트(튜플, 문자열):
    명령문
    ...
"""

lst = [1,3,5,7,9]

# 컬렉션 자료형에서 자료를 하나씩 꺼냄
# 컬렉션 데이터의 갯수 만큼 반복
for l in lst:
    print(l)

#%%

# 튜플
for item in 1,3,5,7,9,"end.":
    print(item)

#%%

# 리스트    
for item in [1,3,5,7,9,"end."]:
    print(item)
    

#%%

# 문자열
for item in "Hello, world!":
    print(item)
    
#%%

# set : 중복을 허용하지 않음, 순서 보장하지 않음
for item in set("Hello,world!"):
    print(item)
    