'''
# [문제] 계산기 만들기
 1. 다중상속을 이용
 2. 더하기, 뺴기, 곱하기, 나누기 클래스를 각각 정의
 3. 최하위 클래스는 위 2번의 클래스를 다중상속하여
    더하기, 뺴기, 곱하기, 나누기를 수행하는 완전한 클래스를 완성
 '''

# 더하기


class Add():
    def add(self, *args):
        self.result = 0
        for i in args:
            self.result = self.result + i
        print("계산결과:", self.result)

# 뺴기_멀넣어도 양수로나옴


class Minus():
    def minus(self, a, b):
        if a > b:
            self.result = a - b
        elif b > a:
            self.result = b - a
        else:
            self.result = 0
        print("계산결과:", self.result)

# 빼기


class Sub():
    def sub(self, a, b):
        self.result = a - b
        print("계산결과:", self.result)

# 곱하기


class Mul():
    def mul(self, *args):
        self.result = 1
        for i in args:
            self.result = self.result * i
        print("계산결과:", self.result)


# 나누기
class Div():
    def div(self, a, b):
        self.result = a / b
        self.result2 = divmod(a, b)
        print("계산결과:", self.result)
        print('몫:', self.result2[0])
        print('나머지:', self.result2[1])


# 통합
# add minus sub mul div 가능
class Calcu(Add, Minus, Sub, Mul, Div):
    def __init__(self):
        print("계산기 on")

    def on(self):
        print("계산기 on")

    def off(self):
        print("계산기 off")


a = Calcu()
a.sub(4, 7)
a.off()


# %% 계산기 여러버전
# __init__ 사용

class Add():
    def add(self):
        return self.a + self.b


class Sub():
    def sub(self):
        return self.a - self.b


class Mul():
    def mul(self):
        return self.a * self.b


class Div():
    def div(self):
        return self.a / self.bin


class Calcu(Add, Sub, Mul, Div):
    def __init__(self, a, b):
        self.a = a
        self.b = b


# %%
# __init__ 사용x

class Add():
    def add(self, a, b):
        return a + b

class Sub():
    def sub(self, a, b):
        return a - b

class Mul():
    def mul(self, a, b):
        return a * b

class Div():
    def div(self, a, b):
        return a / b

class Calcu2(Add, Sub, Mul, Div):
    def __init__(self):
        pass


# %%
# 선생님버젼
# 값을 하나씩 넣고 누적하면서 계산

# 인터페이스 역할
class CalProto():  # 공통조상: 공통적인 속성, 매서드 정의
    def __init__(self, initval = 0):
        self.tot = initval
        self.cnt = 0
        
    def total(self):
        return self.tot
    
    def avg(self):
        return self.tot / self.cnt

    def count(self):
        self.cnt += 1
        
    def clear(self):
        self.tot = 0
        self.cnt = 0
        
class Add(CalProto):
    def __init__(self, initval = 0):
        super().__init__(initval)

    def add(self, val):
        self.count()     # self.count를 작동시켜 cnt 가 1오름
        self.tot += val


class Sub(CalProto):
    def __init__(self, initval = 0):
        super().__init__(initval)

    def sub(self, val):
        self.count()
        self.tot -= val


class Mul(CalProto):
    def __init__(self, initval = 0):
        super().__init__(initval)

    def mul(self, val):
        self.count()
        self.tot *= val


class Div(CalProto):
    def __init__(self, initval = 0):
        super().__init__(initval)

    def div(self, val):
        self.count()
        self.tot /= val


class Calcu3(Add, Sub, Mul, Div):
    def __init__(self, initval = 0):
        super().__init__(initval)   # 부모의 생성자:

    def total(self):
        return self.tot



a = Calcu3()  # 0
a.add(5)  # 5
a.sub(3)  # 2
a.mul(2)  # 4
a.div(4)  # 1

print("합계:", a.total())
print("평균:", a.avg())

#%%  클리어로 리셋하고 해보기
print("clear")
a.clear()
a.add(99)
a.sub(9)
print("합계:", a.total())
print("평균:", a.avg())
