# 기존 함수로 새로운 함수를 만들려면?
# functools.reduce: 반복가능한 객체의 요소에 차례대로 누적적용하여 이 객체를 하나의 값으로 줄임
# https://docs.python.org/ko/3/library/functools.html

import functools
# functools.reduce(function, iterable)
# reduce()는 입력 받은 컨테이너 타입(iterable)을 지정한 함수에 따라 계산한 후, 단일 값으로 결과를 반환합니다.

data = [1, 2, 3, 4, 5]


def sumfunc(x, y):
    print(f"x({x}), y({y})")
    return x + y


# x는 누적값 y는 iterable 가능한 데이터의 갱신값
# 누적적용(계산)은 왼쪽부터 오른쪽으로
result = functools.reduce(sumfunc, data)
print(result)

# %%
# functools.reduce로 최대값구하기


def func(x, y):
    print(x, y)   # 값이 어떤식으로 들어가는지 확인하게 넣음
    if x > y:
        return x
    else:
        return y


result = functools.reduce(func, [1, 100, 50, 600])
# 한줄로 쓰게 람다로 넣어도됨
# result = functools.reduce(lambda x,y: x if x>y else y, [1, 100, 50, 600])
print(result)

# func(1) 하면은 오류나는데
result2 = functools.reduce(func, [1])  # 이거는 오류안남
print(result2)

# %%

#
def max_val(*args):
    return functools.reduce(lambda x, y: x if x > y else y, *args)


data = [1, 5, 3, 11, 22, 55, 90]

a = max_val(data)
print(a)

#%%
# 재귀호출(자기자신을 다시호출)
# 스택처럼 호출한 함수를 쌓았다가 종료조건을 만나면 위에서부터 하나씩 꺼래 처리하는 방식임
# 점화식과 종료조건만 구현하면 만들 수 있기 때문에 가시성이 높고, 구현하기 쉽다는 장점이 있음
# 단, 1000번(약 997번) 정도까지만 재귀호출이 가능하기 때문에 많은 호출이 필요할 때에는 사용 불가


def recursive(n):
    if n == 1:  # 1 일때 끝남
        return n
    return n * recursive(n-1)   

a = recursive(5)  # 5 * 4 * 3 * 2  # 1에는 리턴
print(a)

#%% 재귀호출
# 최대공약수
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
    
print(gcd(192,162)) # 6
