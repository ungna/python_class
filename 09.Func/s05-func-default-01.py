# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:59:45 2023

@author: Solero
"""

# 함수
# 파라미터의 디폴트 값(default value)
# 기본값을 지정하면 호출할 때 인자값을 생략할 수 있다.

#%%

# 파라미터 z의 기본값 : 0.1
def move(x, y, z=0.1):
    print(f"move(x:{x},y:{y},z:{z})")
    
    
#%%

move(10, 20, 30)    

#%%

# z값을 생략하면 기본값 0.1이 출력
move(10, 20)    
move(x=11, y=12)
move(y=22, x=33)
move(y=22, x=33, z=10)
move(10,20,z=30)







