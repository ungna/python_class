# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:27:52 2023

@author: Solero
"""

# collections.deque : 데크
# 양방향 자료형
# 큐(queue)   : FIFO(First In First Out), 선입선출
# 스텍(stack) : LIFO(Last In First Out), 후입선출

#%%

from collections import deque

a = [1,3,5,7,9]
q = deque(a)


#%%

# 참조만 하기 때문에 데이터는 사라지지 않는다.
for r in q: # 데크의 처음부터 참조
    print(r)

print(q)    

#%%

# 큐(Queue): FIFO
# pop() : 꺼내면 기존 데이터 사라짐
# 맨 마지막 데이터 : 9를 꺼내고 지움
r = q.pop()
print("pop() : result=", r, "deque=", q)

#%%

# 마지막 데이터부터 하나씩 꺼냄
while q:
    r = q.pop()
    print(r)

print(q)


