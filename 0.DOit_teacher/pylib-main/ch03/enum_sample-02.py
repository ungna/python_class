# enum
# 상수집합: 열거형 상수
# 상수형태 대문자

from datetime import date
from enum import IntEnum

# class Week(IntEnum):
class Week: # 클래스 변수: 객체화가 되지 않아도 사용 가능(static variable)
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


#%%
# 클래스 변수는 수정 가능
Week.WEDNESDAY = -1
print(Week.WEDNESDAY)

#%%

def get_menu(input_date):
    menu = { # dict
        Week.MONDAY: "김치찌개",
        Week.TUESDAY: "비빔밥",
        Week.WEDNESDAY: "된장찌개",
        Week.THURSDAY: "불고기",
        Week.FRIDAY: "갈비탕",
        Week.SATURDAY: "라면",
        Week.SUNDAY: "건빵",
    }
    
    print(input_date, ": 요일=", input_date.isoweekday()) # 수요일 : 3
    return menu[input_date.isoweekday()] # KeyError: 3


print(get_menu(date(2023, 8, 30)))
print(get_menu(date.today())) 


