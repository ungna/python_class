# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:00:55 2023

@author: Solero
"""

# 클래스
# 다중상속
# 상속된 부모 클래스들에서 동일한 메서드가 있으면
# 먼저 상속된 클래스의 메서드가 사용된다.

#%%
class A:
    def printval(self, val):
        print("[A] val=", val)
        
#%%

class B:
    def printval(self, val):
        print("[B] val=", val)

#%%

class C(B,A):
    pass


#%%
c = C()
c.printval(10) # [B] val= 10


