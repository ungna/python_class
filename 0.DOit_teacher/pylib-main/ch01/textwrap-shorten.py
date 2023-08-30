# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 08:53:24 2023

@author: Solero
"""
# https://docs.python.org/ko/3/library/textwrap.html
# 001 문자열을 줄여 표시하려면? ― textwrap.shorten

import textwrap

textwrap.shorten("Life is too short, you need python", width=15)

#%%

textwrap.shorten("인생은 짧으니 파이썬이 필요해", 
                 width=15, placeholder='---')
