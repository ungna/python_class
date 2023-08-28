# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:22:28 2023

@author: Solero
"""

"""
[문제] 전자계산기
1. 다중 상속을 이용
2. 덧셈, 뺄셈, 나눗셈, 곱셈 클래스를 각각 정의
3. 최하위 클래스는 위 2번의 클래스를 다중상속하여 
4. 덧셈, 뺄셈, 나눗셈, 곱셈을 수행하는 완전한 클래스를 완성
"""

#%%

class Plus:
    def __init__(self, initval=0):
        self.tot = initval
        
    def plus(self, val):
        self.tot += val
        
#%%
class Minus:
    def __init__(self, initval=0):
        self.tot = initval
        
    def minus(self, val):
        self.tot -= val
        
#%%        

class Multiple:
    def __init__(self, initval=0):
        self.tot = initval
        
    def multiple(self, val):
        self.tot *= val
        
#%%

class Divide:
    def __init__(self, initval=0):
        self.tot = initval
        
    def divide(self, val):
        self.tot /= val
        
#%%

class Calc(Plus, Minus, Multiple, Divide):
    def __init__(self, initval=0):
        super().__init__(initval) # 부모의 생성자 : Plus.__init__()
    
    def total(self):
        return self.tot

#%%

calc = Calc(10)  # tot: 10
calc.plus(5)     # tot: 15
calc.minus(3)    # tot: 12
calc.multiple(2) # tot: 24
calc.divide(4)   # tot: 6
print("합계:", calc.total())

#%%

calc = Calc()    # tot: 0
calc.plus(5)     # tot: 5
calc.minus(3)    # tot: 2
calc.multiple(2) # tot: 4
calc.divide(4)   # tot: 1
print("합계:", calc.total())
