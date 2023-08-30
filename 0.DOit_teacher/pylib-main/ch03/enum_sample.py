# enum
# 상수집합: 열거형 상수
# 상수형태 대문자

from datetime import date
from enum import IntEnum


# 클래스 변수의 형태
class Week(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


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
    return menu[input_date.isoweekday()]

print(get_menu(date(2020, 12, 6)))
print(get_menu(date(2020, 12, 18)))

#%%

# 값을 수정할 수 없다.
# AttributeError: cannot reassign member 'MONDAY'
Week.MONDAY = -1
print(Week)
