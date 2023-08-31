# 기존 함수로 새로운 함수를 만들려면?
# functools.partial: 하나 이상의 인수가 이미 채워진 새 버전의 함수를 만들때 사용
# https://docs.python.org/ko/3/library/functools.html

# 덧셈, 곱셈을 수행하는 함수
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:  # 여기서는 * 안붙이고 씀
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


print('덧셈: ', add_mul("add", 1, 2, 3, 4, 5))
print("곱셈: ", add_mul("mul", 1, 2, 3, 4, 5))

# %%
# 기존함수(add_mul)을 활용하여 add() mul() 함수를 만듬
# 일반코드


def add(*args):
    # 가변인자를 다른 함수의 인자로 전달할때 아스터리스크(*)를 안붙이면 오류남
    #    -> 가변인자 전체를 튜플로 묶어서 개별 인자가 아니라 하나의 튜플로 넘어옴 ((1,2,3,4,5))
    # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
    return add_mul('add', *args)


def mul(*args):
    return add_mul('mul', *args)


print(add(1, 2, 3, 4, 5))
print(mul(1, 2, 3, 4, 5))

# %%
# functools.partial 사용
# 기존 함수를 이ㅛㅇㅇ해서 새로운 함수를 만든다

from functools import partial

add = partial(add_mul, "add")
mul = partial(add_mul, "mul")

print(add(1, 2, 3, 4, 5))
print(mul(1, 2, 3, 4, 5))

#%%

# functools.partial 응용
# 기존 add에 하나 이상의 인수를 미리 채워서 새버전의 함수를 만듬

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:  
            print(i)   # 더하기 전에 print를 넣어서 인자가 들어간 순서확인
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


add_100 = partial(add_mul, "add", 100) # add_mul의 add에서 *arg에 기본으로 100이 제일 앞에 들어가있음
print(add_100(1, 2, 3, 4, 5))    # 100,  1,2,3,4,5 

mul_2_3 = partial(add_mul, "mul", 2, 3)  # add_mul의 mul에서 *arg에 기본으로 2, 3이 제일 앞에 들어가있음
print(mul_2_3(1,2,3,4,5))    # 2,3, 1,2,3,4,5



# %%
# 가변인자를 다른 함수의 인자로 전달할때 아스터리스크(*)를 안붙이면 오류남
# * 안붙이고 넘어왔을때
def addx(*args):
    print("args:", type(args), args)
    result = 0
    for ag in args:  # 튜플((1, 2, 3, 4, 5),) 로 넘어온거를 풀음
        for i in ag:
            result = result + i
    return result


def add(*args):
    # 아스터리스크(*)를 안붙힘  => (1,2,3,4,5)를 하나의 인자로 보고 묶어서 보냄
    return addx(args)


print(add(1, 2, 3, 4, 5))
