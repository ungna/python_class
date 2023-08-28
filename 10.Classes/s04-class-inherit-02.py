# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:14:38 2023

@author: Solero
"""
#%%
"""
# 클래스(class)
# 상속(inheritance) 
#   - 다중 상속 지원
#
# 정의
class 자식클래스(부모클래스, [다른부모클래스, ...]):
    ...
"""

#%%
class Student: # 학생 시험 점수 클래스
    
    def __init__(self, name="아무개"): # 생성자
        print(f"[Student] __init__({name}) : self({self})")
        # 멤버변수 선언
        self.name = name
        self.tot = 0
        self.kor = 0
        self.eng = 0
        
    def __del__(self): # 소멸자
        print(f"[Student] __del__({self.name}) : self({self})")
        
    def korean(self, val): # 국어점수
        self.sum(self.kor, val)
        self.kor = val
        
    def english(self, val): # 영어점수
        self.sum(self.eng, val)
        self.eng = val
        
    def sum(self, sub, add):
        self.tot -= sub
        self.tot += add 
        
    def total(self):
        return self.tot

    def score(self): # 점수 출력
        print("이름:", self.name)
        print("국어:", self.kor)
        print("영어:", self.eng)
        print("-" * 12)
        print("총점: ", self.tot)
   
#%%        

# Student 클래스를 상속하여 새로운 클래스 School를 정의
class School(Student):
    def average(self): # 기능확장
        return self.tot / 2

#%%

s2 = School("우등생")
s2.korean(100)
s2.english(100)
s2.score()
print("평균: ", s2.average())
