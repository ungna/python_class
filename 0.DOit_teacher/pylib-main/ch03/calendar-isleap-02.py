# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:54:14 2023

@author: Solero
"""
# https://docs.python.org/ko/3/library/calendar.html
# 윤년
# calendar.isleap(연도)

import calendar

# year = 2020 # 윤년
# year = 2022 # 평년
# year = 2024 # 윤년
year = 400 # 윤년
isleap = calendar.isleap(year)

tfleap = "윤년" if isleap else "평년"

print(f"({year})년은 {tfleap}입니다.")

#%%

# [문제] 함수 isleap(연도)를 만들어 
# 윤년이면 True, 평년이면 False를 리턴
# 조건 : 라이브러리를 사용하지 않고 작성하라.
# - 윤년은 
#   1. 4년에 한 번씩 온다.
#   2. 100년에 한 번씩 안온다.
#   3. 400년에 한 번씩 온다.
# 검증:
#   1. 1부터 3000까지 반복문으로 처리    
#   2. calendar.isleap(year)과 비교하여
#      틀리면 오류 메시지 출력

#%%

import calendar

def isleap(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

print(isleap(4), calendar.isleap(4))
print(isleap(100), calendar.isleap(100))
print(isleap(400), calendar.isleap(400))
print(isleap(2020), calendar.isleap(2020))

for year in range(3001):
    if isleap(year) != calendar.isleap(year):
        print(f"{year}년도가 잘못되었습니다.")
        break
else:
    print("검증: 정상입니다.")
    



