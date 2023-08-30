# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:24:40 2023

@author: Solero
"""

# 002 긴 문장을 줄 바꿈하려면? ― textwrap.wrap

long_text = 'Life is too short, you need python. ' * 10
print(long_text)

#%%

# 지정된 넓이(width) 만큼 라인 단위로 잘라서 리스트로 리턴
# 단어 단위로 문자열을 자르므로 단어 중간이 끊어지지는 않는다.

import textwrap
long_text = 'Life is too short, you need python. ' * 10
result = textwrap.wrap(long_text, width=70)
print('result len:', len(result)) # list
print(result)

#%%
for lst in result:
    print(lst)
    
#%%

# result 결과를 line-feed 넣어서 하나의 문자열로 구성
# 
lfresult = '\n'.join(result)
print(lfresult)

#%%

result = textwrap.fill(long_text, width=70)
print(result)

    