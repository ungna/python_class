# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:32:54 2023

@author: Solero
"""

# 정규 표현식
"""
[2023-08-29 10:15:31:009] [WARN] 통신장비 통신 장애 발생
"""

# 날짜 패턴
import re


p = re.compile("[0-9.\-/]+") # 패턴을 컴파일

s1 = "[2023-08-29 10:15:31:009] [WARN] 통신장비 통신 장애 발생"
s2 = "[2023/08/30 10:15:31:009] [WARN] 통신장비 통신 장애 발생"
s3 = "[23/08/31 10:15:31:009] [WARN] 통신장비 통신 장애 발생"
s4 = "[23.09.01 10:15:31:009] [WARN] 통신장비 통신 장애 발생"

strlist = [s1,s2,s3,s4]

for s in strlist:
    m = p.search(s)
    if m != None:
        print('m.span:', m.span(), type(m.span())) # <class 'tuple'>
        sp, ep = m.span() # 시작위치, 마지막위치
        print(f"매치된 문자열: ({ s[sp:ep]})")
        
        
        
        
        