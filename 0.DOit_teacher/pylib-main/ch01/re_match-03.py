# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:32:54 2023

@author: Solero
"""

# 정규 표현식

import re

# 반드시 알파벳으로 시작
# 소문자 a부터 z까지의 임의 문자가 1번 이상 나오는 패턴
# 문자열의 처음부터
p = re.compile("[a-zA-Z, .]+") # 패턴을 컴파일

s = "Hello, world."
m = p.match(s)
if m != None:
    print('m.span:', m.span(), type(m.span())) # <class 'tuple'>
    sp, ep = m.span() # 시작위치, 마지막위치
    print("매치된 문자열:", s[sp:ep])