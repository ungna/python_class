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
# 데크와 리스트의 차이

lst = [1,3,5,7,9]
print(lst)
#%%

# list.pop(index)

print("pop() :", lst.pop(), lst)    # 맨 마지막 요소를 꺼내고 지움
print("pop(0) :", lst.pop(0), lst)  # 맨 처음 요소를 꺼내고 지움
print("pop(2) :", lst.pop(2), lst)  # 지정된 인덱스 요소를 꺼내고 지움

