# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:20:33 2023

@author: Solero
"""

# 함수(Function)
# 1. 함수는 호출하기 전에 정의가 되어 있어야 한다.
# 2. 함수의 리턴값이 없는 경우 리턴값을 받으면 None이다.
# 3. 함수 정의에서 리턴값이 없으면 return을 생략하면 된다.
# 4. 함수 정의에서 파라미터가 없으면 함수() 형태로 파라미터를 생략한다.
#
# 함수 장점:
#  1. 모듈화: 기능별로 분리
#  2. 블랙박스화: 처리과정보다는 결과   
#  3. 코드의 재사용
#
# 매개변수와 인수
# 매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수, 함수 정의
# 인수(arguments) : 함수를 호출할 때 전달하는 입력값, 함수 호출


"""
함수정의

def 함수명(파라미터):
    명령문
    return 리턴값

"""

#%%
# 함수정의
# 파라미터 : None
# 리턴값: None
def hello():
    print("hello() : ", end='')
    print("Hello, World")

#%%
# 함수호출    
hello()    
hello()    
hello()    

#%%
# 리턴값이 없음 : None
print("리턴값:", hello())


