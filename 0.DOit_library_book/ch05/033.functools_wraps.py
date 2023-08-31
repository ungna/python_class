# wrapper 함수의 속성을 유지하려면?  이해X
# wrapper 함수: 실제함수를 감싼 함수로 실제 함수 호출시 특별한 동작을 하도록 기능을 덧붙인 함수
# wrapper함수를 정의할때 함수의 이름이나 설명문 같은 속성을 유지하게함- 데코레이터를 만들때 사용
# wrapper을 하기전에 closure, decorator을 알아야됨
# https://docs.python.org/ko/3/library/functools.html


# closure: 내부함수를 구현하고 그 내부함수를 반환하는 함수
# 즉 외부함수를 실행하면은 바로 값이 나오는게 아니고 또다른 함수가나옴

# 클로저함수
# 클로저함수에서는 외부함수에서 결정된 것은 내부함수에서 변경이 안됨
def mul(m):   # 외부함수

    def wrapper(n):  # 내부함수
        return m * n    # mul3에서는 m은 3으로 고정되고 변경이 안됨
    
    return wrapper


# mul은 클로져함수라 내부함수로 연결되고 특정한 값이 안나옴
print(mul(m=3))


mul3 = mul(m=3) # 3을 곱하는 함수 
mul5 = mul(m=5)  # 5를 곱하는 함수

print(mul3(n=10))  # 3을 곱하는 함수에 10을 넣음
print(mul5(n=10))  # 5을 곱하는 함수에 10을 넣음

#%% 
# class를 사용
class Mul:
    def __init__(self, m):  # 생성자
        self.m = m
    
    def mul(self, n):
        return self.m * n
    
    
mul3 = Mul(3) 
mul5 = Mul(5)

print(mul3.mul(10))  #30
print(mul5.mul(10))  #50

#%%

# __call__: 클래스의 객체를 함수처럼 호출하는 매서드
class Mul:
    def __init__(self, m):  # 생성자
        self.m = m
        
    # call을 사용해 Mul.함수() 이런식으로 호출 안하고 class안의 함수를 사용
    def __call__(self, n):  
        return self.m * n
    

mulx = Mul(3) # Mul클래스로 만들어서 mulx에 Mul(3)을 넣어 mulx.mul() 이런식으로 호출안하고 바로 mulx()로 사용
mul5 = Mul(5) 

print(mulx(10))  # 30
print(mul5(10))  # 50


#%%

# wrap
import functools
import time


def elapsed(original_func):
    @functools.wraps(original_func)  # 여기에 추가!!  # 이거빼면은 어케될까?
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result

    return wrapper


@elapsed
def add(a, b):
    """ 두 수 a, b를 더한값을 리턴하는 함수 """
    return a + b


print(add)  # 함수명 출력
help(add)  # 함수의 독스트링 출력

#%%
def elapsed(original_func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result

    return wrapper

@elapsed
def add(a, b):
    """ 두 수 a, b를 더한값을 리턴하는 함수 """
    return a + b


print(add)  # 함수명 출력
help(add)  # 함수의 독스트링 출력