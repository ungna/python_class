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

a = [1,2,3,4,5]

print(a)

# 시계방향 회전
q = deque(a)
print(q, id(q))
q.rotate(2)
r = list(q)
print("list:", r, id(r))

#%%

# 시계 반대 방향을 회전
q.rotate(-2)
print(q, id(q))
r = list(q)
print("list:", r, id(r))
