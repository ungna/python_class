# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:14:38 2023

@author: Solero
"""

# 클래스(class)
# 생성자 : __init__(self), 객체가 메모리에 생성될 때 호출
# 소멸자 : __del__(self), 객체가 메모리에서 사라질 때 호출

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

s1 = Student("차등생")
s1.korean(100)
s1.english(90)
s1.score()
print("평균: ", s1.total() / 2)

#%%

# 기존의 객체에 새로운 객체를 할당
# 기존 객체의 소멸자(__del__)가 호출된다.

s1 = Student("우등생")
s1.korean(100)
s1.english(100)
s1.score()
print("평균: ", s1.total() / 2)


