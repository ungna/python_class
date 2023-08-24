# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:40:41 2023

@author: Solero
"""

# 조건부 연산자(conditional expression)
# 변수 = 참 if 조건 else 거짓

#%%

"""
[문제]
# 점수에 따른 등급을 부여한다.
# 조건: 
#   - 점수의 범위는 0점에서 100점 사이여야 한다.
#   - 범위를 넘어서면 "잘못된 점수"라고 출력한다.
# A등급 : 90점 이상
# B등급 : 80점 이상
# C등급 : 70점 이상
# D등급 : 60점 이상
# E등급 : 60점 미만

# 일반 if문으로 처리
# 조건부 연산자(conditional expression)으로 처리ㅣ
"""

#%%

# score = -110
score = 99
grade = None

# 일반 조건문
if score >= 0 and score <= 100:
    if score < 60:
        grade = 'E'
    elif score < 70:
        grade = 'D'    
    elif score < 80:
        grade = 'C'    
    elif score < 90:
        grade = 'B'    
    else:
        grade = 'A'    
else:    
    grade = "'잘못된 점수'"

print(f"<1> 점수는 {score}점이며 등급은 {grade}이다")    


#%% 

# 조건부 연산자(conditional expression)으로 처리
score = -10
grade = None

grade = 'A' if score >= 90 and score <= 100 \
    else 'B' if score >= 80 and score < 90 \
    else 'C' if score >= 70 and score < 80 \
    else 'D' if score >= 60 and score < 70 \
    else 'E' if score >= 0 and score < 60 \
    else "'잘못된 점수'"        

print(f"<2> 점수는 {score}점이며 등급은 {grade}이다")   
