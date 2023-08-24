# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:54:26 2023

@author: Solero
"""

# 반복문 : while
# while문의 조건식이 참이면 해당 블럭을 반복 실행

#%%

# [문제]
# 정기예금 복리계산
# 원금 10만원, 이자가 연10%, 만기 10년, 복리로 계산하라.

total = 100000 # 원금
last = 10      # 10년
interest = 0.1 # 이자율
cnt = 1        # 년수

while cnt <= last:
    cost = total * interest # 이자
    total += cost
    print(f"cnt({cnt}, cost({cost}), total({total})")
    cnt += 1
    
totinter = total - 100000    
print(f"총이자: {totinter}")    
print(f"총금액: {total}")    

#%%

# [문제]
# 정기적금 복리계산
# 연불입금 10만원, 이자가 연10%, 만기 10년, 복리로 계산하라.

paid = 100000  # 매년 적금
total = paid   # 원금
last = 10      # 10년
interest = 0.1 # 이자율
cnt = 1        # 년수

while cnt < last: # 첫 달은 이자 없음
    total += paid
    cost = total * interest # 이자
    total += cost
    print(f"cnt({cnt}, cost({cost}), total({total})")
    cnt += 1
    
totinter = total - (paid * last)    
print(f"총이자: {totinter}")    
print(f"총금액: {total}")    
