# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:14:38 2023

@author: Solero
"""

# 클래스(class)
# 객체지향 프로그래밍: 객체, 인스턴스
# 속성: 동일한 자료들의 그룹, 멤버 변수, 공개(정보은폐를 지원하지 않음)
# 함수: 멤버 함수, 메서드, 멤버 변수를 접근할 수 있는 함수

#%%


# 한 명의 학생의 점수
score = 90
print("학생의 점수:", score)

#%%

# 여러명의 학생의 점수
# 여러 과목의 학생의 점수
# 변수의 학생의 수, 과목의 수 만큼 계속 선언

# 1번 학생의 국어, 영어 점수
k1 = 90
e1 = 80

# 2번 학생의 국어, 영어 점수
k2 = 100
e2 = 99

#%%

# 클래스 정의
# 클래스 이름 : Student
# 멤버변수 : self.kor, self.eng, 없으면 새로 만들고 있으면 사용
# 멤버함수 : korean(), english(), score()
# self : 객체 식별자
# 메소드를 호출 할 때 self를 생략

class Student: # 학생 시험 점수 클래스
    def korean(self, val): # 국어점수
        self.kor = val
        
    def english(self, val): # 영어점수
        self.eng = val

    def score(self): # 점수 출력
        print("국어: ", self.kor)
        print("영어: ", self.eng)
   
#%%        

# 클래스를 객체화

# 1번학생        
s1 = Student()
s1.korean(100)
s1.english(99)
print("[1번 학생 점수]")
s1.score()
print("멤버변수는 공개이므로 메소드를 통하지 않고 접근 가능")
print("국어: ", s1.kor)
print("영어: ", s1.eng)

#%%
# 2번학생        
s2 = Student()
s2.korean(88)
s2.english(77)
s2.score()

#%%

print("s1 == s2 ?", s1 == s2) # False
        
print("type(s1)", type(s1))
print("type(s2)", type(s2))



