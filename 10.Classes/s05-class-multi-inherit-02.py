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
    def __init__(self, val):
        self.cnt = val
        
    def printval(self, val):
        print("[A] val=", val)
        
    def a(self):
        return 'a'
        
#%%

class B:
    def __init__(self, val):
        self.cnt = val * 2
        
    def printval(self, val):
        print("[B] val=", val)
    
    def b(self):
        return 'b'

#%%

class C(A,B):
    def count(self):
        return self.cnt # 부모(A)의 멤버변수를 참조

class D(B,A):
    def count(self):
        return self.cnt # 부모(B)의 멤버변수를 참조

#%%
c = C(7)
print(c.a(), c.b(), "count=", c.count()) # 7
c.printval(10) # [A] val= 10

#%%
d = D(7)
print(c.a(), c.b(), "count=", d.count()) # 14
d.printval(10) # [B] val= 10

