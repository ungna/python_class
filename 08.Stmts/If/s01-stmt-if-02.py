# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 10:06:44 2023

@author: Solero
"""

#%%
money = False

if money != True:
    print("참이다.")
else:
    print("거짓이다.")
    
#%%    

money = False

if money == True:
    print("참이다.")
else:
    print("거짓이다.")
    
#%%

# 권고하지 않음: 0,1로 참, 거짓을 판별하는 것
# True, False 사용

money = 1 # 참

if money == True:
    print("참이다.")
else:
    print("거짓이다.")

#%%

money = 0 # 거짓

if money == True:
    print("참이다.")
else:
    print("거짓이다.")
    
#%%

money = "1000"    # 참

if money:
    print("돈을 가지고 있다.")
else:
    print("돈이 없다.")

#%%

money = ""    # 거짓

if money:
    print("돈을 가지고 있다.")
else:
    print("돈이 없다.")
    
#%%

money = None # 참이 아니다.
print(type(money)) # <class 'NoneType'>

if money:
    print("돈을 가지고 있다.")
else:
    print("돈이 없다.")
    
#%%

money = None # 참이 아니다. (모른다)
print(type(money)) # <class 'NoneType'>

if money == True:
    print("돈을 가지고 있다.")
elif money == False:   
    print("돈이 없다.")
else:
    print("모른다.")
    





