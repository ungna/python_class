'''
# 클래스(class)
# 객체지향 프로그래밍: 객체, 인스턴스
# 속성: 동일한 자료들의 그릅, 맴버 변수
# 함수: 맴버 함수, 매서드, 맴버 변수를 접근할 수 있는 함수(정보은폐)
# 파이썬은 진정한 의미에서 객체지향은 아님 
   # why? 통제가 안되서 
   #    자바의 경우는 private 등으로 통제가 가능하지만 파이썬은 오픈임

# 클래스는 프로그래밍에 반드시 필요한 것은 아니지만 적재적소에 사용하면 얻는 이익이 많다

# 클래스 시작은 대문자로
# 맴버함수 이름은 소문자로 시작 
# 클래스에 첫 맴버변수는 self로 넣어야됨
'''

# 예제
# 학생의 점수
score = 90
print("학생의 점수:", score)

# 다수의 학생의 점수
# 1번 학생의 국어영어
k1 = 90
e1 = 100

# 2번 학생의 국어영어
k2 = 88
e1 = 77

# %%
# 클래스화
# 코드량은 많아질 수 있으나 점더 체계적으로 관리할 수 있음
# self: 객체 식별자,  자바의 this랑 비슷함
# 파이썬에서는 self를 메서드의 펏 매개변수로 self를 넣어야됨
# 객체를 호출할때 this처럼 객체를 불러오는거
# 클래스 이름: Student
# 멤버변수: self.kor, self.eng
# 맴버함수: k_score(), e_score(), score()


class Student:  # 학생 시험점수 클래스 이름
    def k_score(self, val):  # 국어점수
        self.kor = val

    def e_score(self, val):  # 영어점수
        self.eng = val

    def score(self):  # 점수 출력
        print("국어:", self.kor)
        print("영어:", self.eng)



# 1번 학생 클래스 객체화
# 자바와 다르게 new 사용x 일반선언하듯이
s1 = Student()    # 여기서 self = s1

# 클래스 사용
s1.k_score(90)    # 사용할떄 self를 쓰지는 않는다
s1.e_score(100)
s1.score()

# 2번 학생 클래스 객체화
s2 = Student()

# 클래스 사용
s2.k_score(88)
s2.e_score(77)
s2.score()

# %%
# 맴버변수는 공개라서으로 매서드(settergetter같은거인듯?)를 통하지 않고 접근 가능
# 자바와 다르게 private가 없고 오픈이라서
print(s1.kor)
print(s2.eng)

#%% 
# 생성자: __init__(self): 객체가 메모리에서 생성될때 호출

class Student:  # 학생 시험점수 클래스 이름
    def __init__(self, name):  # 생성자
        print(f"[Student] 생성자: self({self})")
        self.name = name
        self.tot = 0

    def k_score(self, val):  # 국어점수
        self.kor = val

    def e_score(self, val):  # 영어점수
        self.eng = val
    
    def total(self):      # 총점 
        self.tot = self.kor + self.eng
        return self.tot

    def score(self):  # 점수 출력
        print("이름:", self.name)
        print("국어:", self.kor)
        print("영어:", self.eng)
        print("총점:", self.tot)


    
s3 = Student("한파이썬")
s3.k_score(50)
s3.e_score(60)
s3.total()      # 리턴이 없어서 출력이 안됨
s3.score()


#%% total 다른방식으로_1

class Student:  # 학생 시험점수 클래스 이름
    def __init__(self, name):  # 생성자
        print(f"[Student] 생성자: self({self})")
        self.name = name
        self.tot = 0
        self.kor = 0
        self.eng = 0

    def k_score(self, val):  # 국어점수
        self.tot = self.tot - self.kor  # 점수가 수정됬을때 수정전 값을 제거  # 누적되면 안되니까
        self.tot = self.tot + val       # 수정된 값을 더해줌
        self.kor = val                 # 수정된 값 설정

    def e_score(self, val):  # 영어점수
        self.tot = self.tot - self.eng
        self.tot = self.tot + val       
        self.eng = val
    
    def total(self):      # 총점 
        return self.tot

    def score(self):  # 점수 출력
        print("이름:", self.name)
        print("국어:", self.kor)
        print("영어:", self.eng)
        print("총점:", self.tot)
        
        
s4 = Student("생성자때문에이름넣어야됨")
s4.k_score(60)
s4.k_score(70)    # 점수 수정
s4.e_score(100)
s4.total()     # 리턴이 없어서 출력이 안됨
s4.score()

#%% total 다른방식으로_2

class Student:  # 학생 시험점수 클래스 이름
    def __init__(self, name = "default"):  # 생성자 default값 추가
        print(f"[Student] 생성자: self({self})")
        self.name = name
        self.tot = 0
        self.kor = 0
        self.eng = 0

    def k_score(self, val):  # 국어점수
        self.sum(self.kor, val)  # 점수가 수정된걸 sum으로 넘김
        self.kor = val                 # 수정된 값 설정

    def e_score(self, val):  # 영어점수
        self.sum(self.eng, val)
        self.eng = val
    
    def sum(self, sub, add):   
        self.tot -= sub         # 넘어온 self.kro self.eng는 sub로 들어가서 빼고 
        self.tot += add         # val은 sub로 들어가서 더해줌
        
    def total(self):      # 총점 
        return self.tot

    def score(self):  # 점수 출력
        print("이름:", self.name)
        print("국어:", self.kor)
        print("영어:", self.eng)
        print("총점:", self.tot)
        
        
s4 = Student() # default 넣어서 안넣어도됨
s4.k_score(60)
s4.k_score(90)    # 점수 수정
s4.e_score(100) 
s4.total()       # 리턴이 없어서 출력이 안됨
s4.score()



#%%  
# 소멸자_del:객체가 메모리에서 사라질때 호출
# 기존의 객체에 새로운 객체를 할당하고 기존의 객체가 사라질때 __del__ 호출
# 소멸자가 없어도 삭제는 되지만 사라지면서 실행

class Student:  # 학생 시험점수 클래스 이름
    def __init__(self, name):  # 생성자
        print(f"[Student] __init__ 이름({name}): self({self})")
        self.name = name
        self.tot = 0
        
    def __del__(self):  # 소멸자
        print(f"[Student] __del__ 이름({self.name}): self({self})")  
        
    def k_score(self, val):  # 국어점수
        self.kor = val

    def e_score(self, val):  # 영어점수
        self.eng = val
    
    def total(self):      # 총점 
        self.tot = self.kor + self.eng
        return self.tot

    def score(self):  # 점수 출력
        print("이름:", self.name)
        print("국어:", self.kor)
        print("영어:", self.eng)
        print("총점:", self.tot)

s1 = Student("한준희")
s1.k_score(88)
s1.e_score(99)

# 한준희가 가고 new한준희가 오면서 삭제되면서 __del__ 에있는 함수가 실행됨
s1 = Student("new한준희")
s1.k_score(88)
s1.e_score(99)


#%% 
# 상속(inheritance): 다른 클래스의 기능을 물려받어 사용
# 기존 클래스를 변경하지 않고 기능을 추가하거나 변경할때 사용
# 2개 이상의 클래스도 상속가능 (자바는 안됨)

# Student1 클래스를 상속하여 새로운 클래스 School 정의

class Student1:  # 학생 시험점수 클래스 이름
    def __init__(self, name):  # 생성자
        print(f"[Student] __init__ 이름({name}): self({self})")
        self.name = name
        
    def k_score(self, val):  # 국어점수
        self.kor = val

    def e_score(self, val):  # 영어점수
        self.eng = val
        
    def score(self):  # 점수 출력
        print("이름:", self.name)
        print("국어:", self.kor)
        print("영어:", self.eng)
        print("총점:", self.tot)
        
class School(Student1):
    pass

s1 = School("학교처음온한준희")   # School에 내용이 없는데 제대로 실행된게 확인됨
s1.k_score(88)
s1.score()

#%%
# 상속_오버라이딩
# 부모와 자식이 같은 이름으로 매서드를 만들면 부모부분이 덮어씌져서(overriding) 자식께 나옴

class Student1:  # 학생 시험점수 클래스 이름
    def __init__(self, name):  # 생성자
        self.name = name
        self.kor = 0
        self.eng = 0
        
    def k_score(self, val):  # 국어점수
        self.kor = val

    def e_score(self, val):  # 영어점수
        self.eng = val
        
    def score(self):  # 점수 출력
        print("이름:", self.name)
        print("국어:", self.kor)
        print("영어:", self.eng)

        
class School(Student1):
    def average(self):
        return (self.kor+self.eng)/2
    
    def score(self):  # 점수 출력 수정
        print("[신기능] 평균:", (self.kor+self.eng)/2)
    
s1 = School("School한준희")   # School에 내용이 없는데 제대로 실행된게 확인됨
s1.k_score(88)
s1.e_score(100)
s1.score()      # 수정하니까 앞에 부분이 덮어씌져서(overriding) 평균만 나옴
                # 밑에 부모 호출하는법 있음

print("")

s2 = Student1("학생한준희")   # Student1함수
s2.k_score(88)
s2.e_score(100)
s2.score()    # 오버라이딩 이전

#%%
# 상속_기능추가_오버라이딩 부모호출
# 부모매서드를 가지고와서 추가만 할 수 있음
# super().매서드 해서 부모 매서드를 가지고오고 밑에 작성해서 내용을 추가할 수 있음

class School2(Student1):
    def average(self):
        return (self.kor+self.eng)/2
    
    def score(self):  # 부모에도 def score가 있어서 오버라이딩됨
        super().score()  # 부모 메서드 호출
        print("[신기능] 평균:", (self.kor+self.eng)/2)  # 추가할 내용
        
        
s1 = School2("School2한준희")   # School에 내용이 없는데 제대로 실행된게 확인됨
s1.k_score(88)
s1.e_score(100)
s1.score() 

#%%
# 상속_다중상속

class X:
    def printx(self, val):
        print("[X] val:", val)
        
class Y:
    def printy(self, val):
        print("[Y] val:", val)
        
class Z(X, Y):
    pass

z = Z()
z.printx("x안에 printx사용")
z.printy("y안에 printy사용")

#%%
# 상속_다중상속
# 동일한 매서드

class A:
    def printval(self, val):
        print("[A] val:", val)
        
class B:
    def printval(self, val):
        print("[B] val:", val)

class C(A, B):
    pass

class D(B, A):
    pass

a = A()
b = B()
a.printval(1)
b.printval(1)

# 상속된 부모 클래스들에서 동일한 매서드가 있으면 먼저 상속된 클래스의 매서드가 사용된다
c = C()
d = D()
c.printval(1)   # [A] val: 1
d.printval(1)   # [B] val: 1

#%%
# 상속_다중상속
# 동일한 매서드,  __init__

class A:
    def __init__(self, val):
        self.cnt = val
        
    def printval(self, val):
        print("[A] val:", val)
        
class B:
    def __init__(self, val):   
        self.cnt = val * 2
    # def __init__(self, val, val2)로 생성자를 설정하면
    # A와 생성자가 달라서 C D로 합치고 사용하려할때 계속 오류남
    # TypeError: B.__init__() missing 1 required positional argument: 'val2'
    
    def printval(self, val):
        print("[B] val:", val)

class C(A, B):
    def count(self):
        return self.cnt  # 부모에 맴버변수를 참조

class D(B, A):
    def count(self):
        return self.cnt  # 부모에 맴버변수를 참조



c = C(7)    # A, B 에서  __init__(self, val) 떄문에 val 값을 넣어야됨
print("__init__ = ", c.count())  # A가 먼저라 7
c.printval(10)

d = D(7)
print("__init__ = ", d.count())  # B가 먼저라 7 * 2
d.printval(10)


#%% 

#[문제]  my_summary0828_class_cal.py에 있음



#%%
'''
# 모듈(mod)
# 함수나 변수, 클래스를 모아 놓은 파이썬 파일
# 외부에서 import해와서 사용함
'''

