# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:57:18 2023

@author: Solero
"""

# 패키지 
#   1. 폴더안에 있는 모듈들
#   2. 파이썬 모듈을 계층적으로 관리

# 폴더 : game/sound/echo.py
# echo.py : soundecho() 함수 
# from game.sound.echo import *
from game.sound.echo import soundecho

# 모듈이름 생략
soundecho("안녕!")

