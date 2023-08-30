# enum
# 상수집합: 열거형 상수
# 상수형태 대문자

from datetime import date
from enum import IntEnum

class Week(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


#%%

# 반복문으로 목록을 추출 가능
for week in Week:
    print("{}:{}".format(week.name, week.value))

#%%

print("일요일: {}:{}".format(Week.SUNDAY.name, Week.SUNDAY.value))

