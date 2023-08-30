# 날짜를 계산하고 요일을 알려면 
# datetime.timedelta: 날짜를 기준으로 몇일 더하고 뺴기 할때 사용
# + - 를 사용

import datetime

# 오늘 날짜
today = datetime.date.today()
print(today)

#%% 
# 오늘로 100일 후 날짜

print("우리가 만난지 100일 후: ", today + datetime.timedelta(days = 100))

# 오늘로 부터 100일 전 
print("우리가 만난지 100일 후: ", today - datetime.timedelta(days = 100))

#%%
# datetime.timedelta(days = )
# days 대신에 seconds, hours, weeks 등 사용가능