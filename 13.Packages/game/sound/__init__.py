# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:16:05 2023

@author: Solero
"""

"""
from game.sound import *
__init__.py 파일의 __all__=[]에 기술된
모듈만 임포트 된다.
"""

# __init__.py

# 모듈이름
__all__ = ['echo','echox']
# __all__ = ['echo']
# __all__ = []

def soundechox(msg):
    print("[game.sound.__init__.py]", msg)

soundechox("__init__")


