# 2월 29일인 해(윤년)를 알려면?
# calendar.isleap: 년, 월, 일로 날짜를 표현할 때 사용하는 모듈

import calendar


# bool 형태로 나옴
calendar.isleap(2023)   # False

calendar.isleap(2024)   # True


#%% 
# calendar.isleap 없이 만들기
## 조건:
# 4로 나누어 떨어지는해
# 그중 100으로 나누어떨어지면 평연
# 그중 400으로 나누어떨어지면 다시 윤년

def is_leap(year):
    if year % 400 == 0 :
        return True
    elif year % 100 == 0 :
        return False
    elif year % 4 == 0 :
        return True
#    elif year == 2999:     # 아래 검증용 
#        return True
    else:
        return False

print(f"2023: {is_leap(2023)}, 2024: {is_leap(2024)}")

# 이렇게도 가능
def isleap(year):
    if year % 4 == 0:
        if (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False
    else:
        return False
#%%
# for문을 이용한 검증

for year in range(1, 3001):
    if is_leap(year) != calendar.isleap(year):
        print(f"기원 {year}년: {is_leap(year)} == ({calendar.isleap(year)})")
        print("검증결과: 잘못된 결과 발견!!")
        break
# for else: for문에서 break를 만나지 않으면 실행
else:
    print("검증결과: 이상없음")









