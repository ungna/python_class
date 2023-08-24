# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:18:34 2023

@author: Solero
"""

#%%
# None
# None은 참도 거짓도 아니다.
# None은 아뭇것도 없다는 의미의 특별한 값

thing = None

if thing:
    print("None은 참이다.")
else:
    print("None은 거짓이다.")
    
# None은 거짓이다.    
    
#%%

thing = None

if thing == True:
    print("thing은 참이다.")
elif thing == False:
    print("thing은 거짓이다.")
elif thing == None:    
    print("thing은 None이다.")
else:
    print("thing은 모른다.")

# thing은 None이다.

#%%
thing = None

if thing is None:    
    print("thing은 None이다.")
else:
    print("thing은 None 아니다.")

# thing은 None이다.