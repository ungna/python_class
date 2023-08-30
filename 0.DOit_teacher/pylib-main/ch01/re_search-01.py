# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:32:54 2023

@author: Solero
"""

# 정규 표현식

import re

# 반드시 알파벳으로 시작
# 소문자 a부터 z까지의 임의 문자가 1번 이상 나오는 패턴
# 문자열에서 탐색 : 임의의 위치에서 처음 만나는 패턴
# 소문자로 시작하고 공백문자는 한 개 이상
# p = re.compile("[a-z]+\s{1,}") # 패턴을 컴파일
p = re.compile("[a-z]+\s+") # 패턴을 컴파일

s = "HELLO, world Weolcome  to korea."
m = p.search(s)
if m != None:
    print('m.span:', m.span(), type(m.span())) # <class 'tuple'>
    sp, ep = m.span() # 시작위치, 마지막위치
    print(f"매치된 문자열: ({ s[sp:ep]})")