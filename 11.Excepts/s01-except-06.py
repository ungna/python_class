# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:53:01 2023

@author: Solero
"""

# 예외처리
# 런타임 오류 처리
# 실행시간에 발생하는 오류 처리
# 런타임 오류가 발생하면 프로그램이 종료


#%%

val = 100
lst = [10,1,3,5,0] # 0,1,2
tot = 0

try:
    for x in lst:
        tot += val / lst[x]     
except:
    print("예외발생: 모든예외처리")
    
print('tot:', tot)    
    
#%%

    
