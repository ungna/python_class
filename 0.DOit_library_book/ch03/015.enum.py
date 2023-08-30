# 숫자에 이름을 붙여 사용하려면?
# enum을 이용해서 상수 집합을 정의

# https://docs.python.org/ko/3/library/enum.html

from enum import IntEnum
from datetime import date


class Week(IntEnum):  # IntEnum을 사용해서 객체지정없이 접근가능 like static
#class Week:    # 이렇게 하면 클래스 변수 
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_menu(input_date):
    menu = {  # dict
        Week.MONDAY: "김치찌개",
        Week.TUESDAY: "비빔밥",
        Week.WEDNESDAY: "된장찌개",
        Week.THURSDAY: "불고기",
        Week.FRIDAY: "갈비탕",
        Week.SATURDAY: "라면",
        Week.SUNDAY: "건빵",
    }
    # menu[키]  # dict니까 key를 입력하면 value가 나옴   
    return menu[input_date.isoweekday()]  # 요일을 숫자로 반환해줌  # weekday는 0부터 시작  isoweekday은 1부터 시작
# datetime.datetime.now().isoweekday()  # 이런식으로 씀


print(get_menu(date(2023, 8, 2)))
print(Week.MONDAY)
#%%
'''
# 클래스 변수는 접근가능
# #class Week: ~~
# Week.MONDAY = -12
print(Week.MONDAY)
'''

#%% 
# 반복문으로 목록을 추출가능
for week in Week:
    print("{}:{}".format(week.name, week.value))


    
    
    
    
    
    