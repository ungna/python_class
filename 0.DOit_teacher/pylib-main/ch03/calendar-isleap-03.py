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

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
#%%
print(f"기원 4년: ({isLeap(4)}) == ({calendar.isleap(4)})")    
print(f"기원 100년: ({isLeap(100)}) == ({calendar.isleap(100)})")    
print(f"기원 400년: ({isLeap(400)}) == ({calendar.isleap(400)})")    
print(f"기원 2020년: ({isLeap(2020)}) == ({calendar.isleap(2020)})")    

#%%

for year in range(1, 3001):
    if isLeap(year) != calendar.isleap(year):
        print("검증: 잘못된 결과가 확인되었습니다.")        
        print(f"기원 {year}년: ({isLeap(year)}) != ({calendar.isleap(year)})") 
        break
else: # for문에서 break를 만나지 않으면 실행
    print("검증: 완벽합니다.")        
    
    