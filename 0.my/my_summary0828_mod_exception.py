'''
# 모듈(mod)
# 함수나 변수, 클래스를 모아 놓은 파이썬 파일
# 외부에서 import해와서 사용함 - 파이썬 확장자 (.py) 생략
# import 묘듈이름
# 사용: 모듈이름.함수(), 모듈이름.변수()
'''

import game.mod.mod1
# import하면서 mod1안에 있는 함수가 실행됨
# game폴더안에 mod폴더안에 mod1

a = 100
b = 200

# mod1 에있는 함수 add를 불러와서 씀
a1 = game.mod.mod1.add(a,b)
b1 = game.mod.mod1.sub(a,b)

print(f"add({a},{b}) -> {a1}")
print(game.mod.mod1.PI)

#%% 

import game.mod.mod2
# if __name__ == "__main__": 가 있어서 호출했을때 아래 코드들이 실행안됨

a = 100
b = 200

# mod1 에있는 함수 add를 불러와서 씀
a1 = game.mod.mod2.add(a,b)
b1 = game.mod.mod2.sub(a,b)

print(f"add({a},{b}) -> {a1}")

#%%
# from 모듈이름 import 모듈함수, 클래스
# 해당 모듈에서 원하는 기능만 선택적으로 임포트
from game.mod.mod2 import Math

a = 10

print(Math.circlearea(a))


#%%
'''
패키지 
 1. 폴더안에 있는 모듈들
 2. 파이썬 모듈을 계층적으로 관리
'''

# 폴더: game/sound/echo.py 
# echo.py : soundecho() 함수
# from game.sound.echo import *
from game.sound.echo import soundecho


# 모듈이름 생략 가능
soundecho("안녕!")

#%%
# 이런식으로 import하면은 
# __init__.py 파일의 __all__ = []에 기술된 모듈만 임포트 된다.
from game.sound import echo

# 여기서는 파일이름.함수 로 써야됨
echo.soundecho("안녕")


#%%
'''
# 예외처리
 런타임 오류처리
 실행시간에 발생하는 오류처리
 런타임 오류가 발생하면 프로그램이 종료
'''

x = 10
y = 0

try:
    # ZeroDivisionError: division by zero
    z = x / y  # 0으로 나누면은 오류남
except ZeroDivisionError as e:
    print("예외발생:", e)

print("결과: ", 0)

#%%

# print("z=", z)   # z 선언안해서 에러뜸
# NameError: name 'z' is not defined

try:
    print("x=", x)
    print("y=", y)
    print("z=", z)   # z 선언안해서 에러뜸
except NameError as e: 
    print("예외발생: ", e)

print("THE END")

#%%
lst = [0,1,2]
#lst[3] = 99
#IndexError: list assignment index out of range

try:
    lst[3] = 99
except IndexError as e:
    print("예외발생:", e)
    
print(lst)



#%%
lst = [1,2,3]
val = 3
total = 0

# 여러개 예외처리
try:
    for x in lst:
        total += val / lst[x]   # lst[3]이 존재하지 않음
        
except ZeroDivisionError as e:
    print("예외발생:", e)
    
except IndexError as e:   # IndexError 발생
    print("예외발생:", e)
    
print(total)

total = 0
# 한번에 여러개
# 먼저 발생된 예뢰를 처리하로 블록을 탈출 = 앞에서 오류있으면 뒤라인 실행안됨
try:
    for x in lst:
        total += val / lst[x]
        
except (ZeroDivisionError, IndexError) as e:
    print("예외발생:", e)
    
    
print(total)

#%% finally

lst = [1,2,3,4,5]
val = 100
total = 0

# 여러개 예외처리
try:
    for x in lst:
        total += val / lst[x]
        
except:  # 모든 예외처리
    print("예외발생하면 실행")
    
finally:  # 예외가 발생되든 되지않든 처리(맨마지막에 있어야됨)
    print("finally: 무조건 처리")
    
print(total)


#%%  else

lst = [1,2,3,4,5]
val = 100
total = 0

# 여러개 예외처리
try:
    for x in lst:
        total += val / lst[x]
        
except:  # 모든 예외처리
    print("예외발생하면 실행")

else: 
    print("else: 예외가 발생되지 않으면 실행")
    
finally:  # 예외가 발생되든 되지않든 처리(맨마지막에 있어야됨)
    print("finally: 무조건 처리")
    
print(total)

#%% 사용자 정의 예외

# Exception 최상위 예외 클래스를 상속받음
class MyError(Exception):
    def __init__(self, say, msg):
        super().__init__(msg)
        self.say = say
#%%

# raise를 쓰면 오류가 강제로 발생됨
# 예외발생
def say_nick(nick):
    if nick == '바보':
        raise MyError("왜","문도~ 바보 아니다~")   
        
    print(nick)

say_nick("엉나")
say_nick("바보")  # MyError 예외발생


#%%

try:
    say_nick("엉나")
    say_nick("바보")
except MyError as e:
    print("예외발생:", e)