# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:18:28 2023

@author: Solero
"""
# https://wikidocs.net/33#time

# 날짜를 계산하고 요일을 알려면

import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

print(day1)
print(day2)
#%%
# 두 날짜의 차이는?

diff = day2 - day1
print(diff.days)

#%%

# 요일은 datetime.date 객체의 weekday 함수를 사용하면 쉽게 구할 수 있다.
# 0:월요일, 1:화요일 ... 6:일요일
day = datetime.date(2023, 8, 29)
week = day.weekday()
print(f"{day}는 ({week})요일") # 1:화요일

#%%

weeks = ('월', '화', '수', '목', '금', '토', '일')

print(f"{day}는 ({weeks[week]})요일") # 1:화요일

#%%

# 오늘날짜
print("today: ", datetime.date.today())

#%%
# 오늘 날짜로부터 몇일 후 날짜?

today = datetime.date.today()
print("우리가 만난지 100일 후: ", today + datetime.timedelta(days=100))

#%%

sd = datetime.datetime(2023, 7, 21)
ed = datetime.datetime(2024, 1, 16)

#%%
td = ed - sd
tt = td * 8 * 5 / 7
print(f"수업일수: 일수({td}), 시간({tt})")

#%%

td = ed - sd
tt = (td / 7) * 5 * 8
print(f"수업일수: 일수({td}), 시간({tt})")






