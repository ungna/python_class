'''
# 함수(Function)
 -> 반복적으로 사용되는 가치가 있는 부분을 한 뭉치로 묶어서 사용하는거
  함수는 호출하기 전에 정의가 되어 있어야 한다
  함수의 리턴값이 없는 경우 리턴값을 받으면 None이 된다
  함수 정의에서 리턴값이 없으면 return을 생략하면 된다
  함수 정의에서 파라미터가 없으면 함수() 형태로 파라미터를 생략한다
     # 입력값 =  파라미터 = 인수 = 매개변수
 
함수의 장점:
    모듈화  - 기능별로 분리 + 프로그램의 흐름 파악 + 어디서 오류가 났는지 쉽게 알수있음
    블랙박스화  - 처리과정보다는 결과 ex) 우리는 print가 어떻게 돌아가는지 모르지만 사용함
    코드의 재사용
    
함수정의 
def 함수명(파라미터):
    명령문
    return 리턴값
'''

# 함수정의
# 파라미터 없음 = 입력값이 없음
# 리턴값 없음 = print를 한거여서 문장을 수행했지 return되는건 없음
def hello():
    print("Hello World")

# 함수호출
hello()
hello()



#%%
# 함수정의
# 파라미터 없음
# 리턴값 있음

def say():
    return "hi"

print(say())
a = say()
print(a)
    
#%% def_return
# 함수 밖에서 선언된 변수는 전역변수(global variables)
a = 10

# 함수 안에서 선언된 변수는 지역변수(local variables)
def test(a):
    # 함수 안에서 생성된 변수는 함수안에서만 유효  -> 밖에서는 효력x
    a = a +10   
    
b = test(a)
print(a)      # 전역변수 10은 그대로 있다
print(b)      # test안에 지역변수 a는 밖으로 나오지 못하고 사라졌다

# 함수 안에서 적용된 것을 밖으로 불러내기 위해 return을 쓴다
# 유사한 것으로 global이 있지만 함수는 독립적으로 존재하는게 좋아서 외부변수에 종속적인 것은 안좋아서 안쓰는게 좋다
def test(a):
    a = a +10   
    return a

b = test(a)
print(a)
print(b)   # 함수가 전달한 지역변수 a는 20 

#%% def_return_다중return
def totalavg(kor, math, eng):
    tot = kor + math + eng
    avg = tot /3
    return tot, avg

# return 하는게 2개여서 변수2개를 ,로 묶어서 선언해야됨
total, average = totalavg(100, 90, 80)     # 튜플로 받아와서 unpacking 한거임
print(f'총점: {total}  평균: {average}')  

#%%
# 함수정의 
# 파라미터가 있음
# 리턴값 없음
def helloa(a):        # 여기서 a에 넣은게 출력됨
    print("Hello", a)
    
# 함수호출
helloa("python")
helloa("Java")
helloa(2)

#%%
# 파라미터 여러개
def many_hello(msg, cnt):
    for x in range(cnt):    # cnt만큼 반복
        print(f'{msg} {x+1}트')  # msg를 넣은 문장 출력

# 매개변수를 생락하고 호출
many_hello("hi", 5)

# 매개변수를 포함하고 호출
many_hello(msg = "hi", cnt = 5)

# 매개변수를 포함하고 호출하면 위치를 다르게 해도됨
many_hello(cnt = 5, msg = "hi")

#%%
# 파라미터가 정수가 아니면은 오류 메시지 리턴
def many_hello(msg, cnt):
    if isinstance(cnt, int) != True:          # cnt의 자료형이 int 가 아니면은 실행
        print( f'cnt ({cnt})의 자료형이 정수가 아닙니다.' )
    else:
        for x in range(cnt):    
            print(f'{msg} {x+1}트')  

many_hello("hi", "hi")
many_hello("hi", 5)

#%% def_default
# 파라미터에 default 설정하기
def many_hello(msg, cnt=2):
    for x in range(cnt):    
        print(f'{msg} {x+1}트')
        
# 초기값을 설정해서 인자값을(여기서는 cnt) 안넣어도 default값이 적용됨
many_hello("hi")      
        
#%% def_*args
# 입력값이 몇개든 상관없는 함수 만들기
# 튜플로 받아와서 쓰는거임
def add_many(*args):      # *args 대신에 *아무거나 해도되지만 관례라 닥치고 *args쓰자
    result = 0
    for i in args:
        result = result + i
    return result

a = add_many(1,2,3,4,5)
b = add_many(1,2,3,4,5,6,7,8,9)

print(f'a는 {a}, b는 {b}')

#%% def_args_len

def average(*args):
    result = 0
    for i in args:
        result = result + i
    average = result / len(args)
    return average

average(10, 20, 30, 40, 50)

#%% def_*args_2

# choice 자리에 'add'넣으면 더하기 'mul'넣으면 곱하기
def add_mul(choice, *args):
    if choice == "add":      # choice자리에 add를 넣으면 더하기 실행
        result = 0
        for i in args:
            result = result + i
        return result
        
    elif choice == "mul":   # choice자리에 mul을 넣으면 곱하기 실행
        result = 1
        for i in args:
            result = result * i
        return result
    else :
        result = "'add'나 'mul'을 넣고 사용해주세요"
        return result

a = add_mul('add', 1,2,3,4)
b = add_mul('mul', 1,2,3,4)
c = add_mul('minus', 1,2,3,4)

print(f'a는 {a}, b는 {b}, c는 {c}')


#%% def_*kwargs
# dictionary 형태로 자료를 받는다

def my(**kwargs):   # *kwargs 대신에 *아무거나 해도되지만 관례라 이하생략
    return kwargs

my_dict = my(name = "DOIT!", price = 22000)
# my_dict = my(name : "DOIT!", price : 22000)  # dict 형태로 인식 못함

print(type(my_dict))
print(my_dict['name'])   
print(my_dict.items())

my_dict2 = my(x = 10, y = 20, a = 10, b = 20, c = 30, d = 40)
print(my_dict2.items())

#%%
# [문제] 지정하는 임의의 인자를 받아서 파라미터의 dict의 키와 값을 출력해라
def unnamed(**kwargs):
    for i in kwargs:
        print(i , kwargs[i])
    
unnamed(x = 10, y = 20, a = 10, b = 20, c = 30, d = 40)


#%% def_pass

# pass를 사용해 아무것도 처리 하지 않는 함수를 만들 수 있음
# API 틀만 만들어 놓고 향후에 기능구현할 예정일때
def empty_func(title, msg, price):
    pass           # return값이 없음

empty_func('','','')



#%% def_pass_사용

# 일부 블록을 pass로 처리할 수 있다.
# why? 기능구현을 아직 안했거나 어케할지 못정해서 일단 pass시킴
def book_list(title, msg, end):
    print(f"title({title}), msg({msg}), end({end})")
    if isinstance(title, str) != True:
        pass      # title이 str로 안들어오면은 어케 처리할지 못정해서 일단 pass한거
    
def book_list_notpass(title, msg, end):
    print(f"title({title}), msg({msg}), end({end})")
    if isinstance(title, str) != True:
        print("tlqksusdk")
    
book_list('a', 'b', 'c')
book_list(123, 'b', 'c')            # pass로 str이 아닐때 머할지 안해서 위에 출력만함
book_list_notpass(123, 'b', 'c')    # pass안하고 기능 넣어서 위에 출력하고 밑에 tlqksusdk가 출력됨


#%% lambda
# def와 동일한 역할을 하는 예약어
# 한줄로 간결하게 만들때사용한다 -> 함수명 생략, return 생략
 # def를 사용할 만큼 복잡하지 않을때 
 # def를 사용하는데 제한이 있는 곳에 사용
 
# lambda_syntax
# function명 = lambda 파라미터 : (return) 수행할거
add = lambda a, b: a + b  # return이 숨어있음
print(add(9,5))

result = add(3, 4)
print(result)

"""
일반함수
def add (a, b):
    return a + b
"""

#%%
# lambda 일회성으로도 사용 가능
print("10^3 => ", (lambda x , y : x ** y)(10, 3))

#%% callback
# callback
# 처리 루틴에게 처리해야할 함수를 전달하여 처리한 결과를 리턴하는 형태
# 함수안에 함수를 넣음 -> 즉 자기대신 일해줄 함수를 불러서 짬떄리는거  
# ex) html 이벤트: 이거 클릭하면 callback(다른함수를 불러서 처리) 해줘

# words: 처리를 해야할 데이터
# callback: 처리해야할 로직이 있는 함수
def soundwonder(words, callback):   # callback 대신 암거나 써도 되지만 이하생략
    for word in words:
        print(callback(word))

words = ['hi', 'good', 'oh', 'nice']

# 첫번쨰 문자를 대문자로 바꾸는 함수
def wonder(word):
    return word.capitalize() + '!'

# wonder라는 함수를 호출하고 이 wonder가 첫 글자를 대문자로 바꾸는 기능이 있음
soundwonder(words, wonder)    

# 매개변수를 포함하고 호출
soundwonder(words = words, callback = wonder)    

#%% lambda_callback
# 할때마나 함수를 호출해야되서 귀찬음
# 람다형식으로 만들어서 해보자

soundwonder(words, lambda word : word.capitalize() + '!')

#%% 함수형 프로그래밍

def score(name):  # 외부함수
    print(f'[score]name: [{name}]')

    
    def minmax(*args): # 내부함수  # callback은 값이 밖에서 안으로 오지만 이건 값을 내부에서 밖으로 보냄
        min = -1  # 점수의 최소값이 0이니까 0이나오더라도 val로 바꿔지게 
        max = -1
        
        for val in args:
            if min == -1 or val < min:
                min = val
            if max == -1 or val > max:
                max = val            
        return name, min, max  # 외부함수에서 받은 값
    
    return minmax  # 내부함수를 리턴

s1 = score("중간고사")  # s1을 호출하면 이떄 부여한 값(중간고사)을 계속 가지고 있음
s2 = score("기말고사")  # s2도 마찬가지

print("중간고사 점수(최소값, 최대값)", s1(100, 90, 60, 70, 80))
print("기말고사 점수(최소값, 최대값)", s2(88, 99, 77, 66, 55, 44))







