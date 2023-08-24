# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:51:29 2023
@author: Solero
"""
# 반복문: for

# range(n)
# range(start, end, start)

#%%
# 0부터 n -1 반복

n = range(10)
for x in n: # 0,1,2,3, ... 9
    print(x)
    
#%%

# 10번 반복
for x in range(10):
    print(x)
    
#%%

# 홀수의 합
odd = 0
for n in range(10): # 0,1,2,3, ... 9
    if n % 2 == 1: # 1,3,5,7,9
        odd += n
        
print("홀수의 합: ", odd)     

#%%

# 짝수의 합
even = 0
for n in range(11): # 0,1,2,3, ... 9, 10
    if n % 2 == 0:  # 0,2,4,6,8,10
        even += n
        
print("변수 for(n)?: ", n)     
print("짝수의 합: ", even)     

#%%

# 홀수의 합
odd = 0
for n in range(1,10,2): # 1,3,5,7,9
    odd += n
    print(f"n({n}), odd({odd})")
        
print("홀수의 합: ", odd)     

   