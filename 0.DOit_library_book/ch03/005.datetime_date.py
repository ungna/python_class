# 날짜를 계산하고 요일을 알려면 
# datetime.date: 년, 월, 일로 날짜를 표현할 때 사용하는 모듈

import datetime

# 날짜 설정
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

print(day1)
print(day2)

#%%
# 오늘 날짜
today = datetime.date.today()
print(today)

#%%
# 두 날짜의 차이는?

diff = day2 - day1
print(diff.days)


#%%

# 요일은 datetime.date 객체의 weekdat함수를 사용하면 쉽게 구할 수 있다
# 0: 월  1: 화  2: 수  3: 목  4: 금  5: 토  6: 일
day = datetime.date(2023, 8, 29)
weeks = ['월','화','수','목','금','토','일']
week = day.weekday() 
print(f"{day}는 {weeks[week]}요일")




