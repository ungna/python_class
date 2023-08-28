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
5. 평균: 연산을 수행한 횟수로 합계를 나눔
"""

#%%

# 프로토타입: 인터페이스 역할
class CalcProto: # 공통조상: 공통적인 속성, 메서드 정의
    def __init__(self, initval=0):
        self.clear(initval)
        
    def total(self):
        return self.tot
    
    def avg(self):
        return self.tot / self.cnt
    
    def count(self):
        self.cnt += 1
        
    def clear(self, initval=0):
        self.tot = initval
        self.cnt = 0
        
#%%    
class Plus(CalcProto):
    def __init__(self, initval=0):
        super().__init__(initval)
        
    def plus(self, val):
        self.count()
        self.tot += val
        
#%%
class Minus(CalcProto):
    def __init__(self, initval=0):
        super().__init__(initval)
        
    def minus(self, val):
        self.count()
        self.tot -= val
        
#%%        

class Multiple:
    def __init__(self, initval=0):
        super().__init__(initval)
        
    def multiple(self, val):
        self.count()
        self.tot *= val
        
#%%

class Divide:
    def __init__(self, initval=0):
        super().__init__(initval)
        
    def divide(self, val):
        self.count()
        self.tot /= val
        
#%%

class Calc(Plus, Minus, Multiple, Divide):
    def __init__(self, initval=0):
        super().__init__(initval) # 부모의 생성자 : Plus.__init__()
    
#%%

calc = Calc(10)  # tot: 10
calc.plus(5)     # tot: 15
calc.minus(3)    # tot: 12
calc.multiple(2) # tot: 24
calc.divide(4)   # tot: 6
print("합계:", calc.total())
print("평균:", calc.avg())

#%%

print("clear...")
calc.clear(1)    # 1값으로 초기화
calc.multiple(99)
calc.minus(90)
print("합계:", calc.total())
print("평균:", calc.avg())

