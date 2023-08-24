# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:54:26 2023

@author: Solero
"""

# 반복문 : while
# 1부터 5까지 1씩 증가시키면서 
# 증가값을 출력하고 증가값의 합을 구하라.

i = 0
s = 0

i += 1
s += i
print(f"i({i}) = 합({s})")

i += 1
s += i
print(f"i({i}) = 합({s})")

i += 1
s += i
print(f"i({i}) = 합({s})")

i += 1
s += i
print(f"i({i}) = 합({s})")

i += 1
s += i
print(f"i({i}) = 합({s})")


#%%

last = 10
i = 0
s = 0

while i < last: # 0, 1, 2, 3, ... 9
    i += 1
    s += i
    print(f"과정: i({i}) = 합({s})")

print(f"최종: i({i}) = 합({s})")
        




