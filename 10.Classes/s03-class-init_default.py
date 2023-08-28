# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:14:38 2023

@author: Solero
"""

# 클래스(class)
# 생성자 : __init__(self)

class Student: # 학생 시험 점수 클래스
    
    def __init__(self, name="아무개"): # 생성자
        print(f"[Student] __init__() : self({self})")
        # 멤버변수 선언
        self.name = name
        self.tot = 0
        self.kor = 0
        self.eng = 0
        
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

# 클래스를 객체화

# 1번학생        
s1 = Student()
s1.korean(100)
s1.korean(90)
s1.english(99)
s1.english(90)
s1.score()

#%%
# 리턴값을 받지 않으면 무시
s1.total() 

print("* 총점: ", s1.total())


