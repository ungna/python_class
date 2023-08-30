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
p = re.compile("[a-z]+")

print("Hello:", p.match("Hello"))
print("hello:", p.match("hello")) # <re.Match object; span=(0, 5), match='hello'>

#%%
print("hello, world:", p.match("hello, world"))
print("hello world:", p.match("hello world"))

# 첫 문자에 공백은 소문자에 매치되지 않음
print("' hello, world':", p.match(" hello, world"))


