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

# 스텍(stack) : LIFO(Last In First Out), 후입선출
r = q.popleft()
print("popleft() : result=", r, "deque=", q)

#%%

# 확인, 참조 : 데이터는 지우지 않음
r = q[1]
print("q[1]:", r, q)

#%%

# pop()에 인덱스를 지정할 수 없다.
# TypeError: deque.pop() takes no arguments (1 given)
# print("q[1]:", q.pop(1))


#%%

# 처음부터 하나씩 꺼내면서 데이터는 지움
while q:
    r = q.popleft()
    print(r)

print(q)


