# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:03:15 2023

@author: Solero
"""

# 함수
# 가변인자: dict
# 파라미터를 딕셔너리로 받음
#%%

# kwargs: { 'x' : 10, 'y': 20, 'z': 30}
def xyz(**kwargs):
    print(f"[xyz] type({type(kwargs)}), {kwargs}")
    print('x=', kwargs['x'])
    print('y=', kwargs['y'])
    print('z=', kwargs['z'])
    
#%%

# TypeError: xyz() takes 0 positional arguments but 3 were given
# xyz(10, 20, 30)    

#%%

# 인자를 하나의 dict로 변환해서 전달
xyz(x=10, y=20, z=30)    

#%%

# TypeError: xyz() takes 0 positional arguments but 1 was given
# 1개의 인자로 인식 : dict 형태가 아니다.
xyz({'x': 10, 'y': 20, 'z': 30})

#%%

# dict 형태이지만 x값 전달
xyz(x={'x': 10, 'y': 20, 'z': 30})

#%%

# 개발 인자 x,y,z가 각각 dict로 해서 전체를 하나의 dict로 전달
xyz(x={'a': 10}, y={'b': 20}, z={'c': 30})









