# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:53:01 2023

@author: Solero
"""

# 예외처리
# 런타임 오류 처리
# 실행시간에 발생하는 오류 처리
# 런타임 오류가 발생하면 프로그램이 종료


#%%

# 사용자 정의 예외

# Exception 최상위 예외 클래스를 상속을 받음
class MyError(Exception):
    def __init__(self, say, msg):
        super().__init__(msg)
        self.say = say
        


#%%

# 예외발생

def say_nick(nick):
    if nick == '바보':
        raise MyError("바보", "나를 무시해서 용서할 수 없습니다.") # 예외 발생
        
    print(nick)

#%%

# MyError 예외 발생
# say_nick('바보')

#%%

try:
    say_nick("천사")
    say_nick("바보")
    say_nick("사람")
except MyError as e:
    print("예외발생:", e.say, ",", e)
    
    
    
    
    
    
    