## 제어문(Control flow statement): 조건문 + 반복문
# if, for, while

## 제어문의 조건으로 bool 사용
# bool : True, False 로 나옴
# [비교연산자]
# <  >  <=  >=  == !=
# [논리연산자]
# and  or  not


#%% if_syntax
# if 뒤에 콜론 넣어야됨

if True:
    print('참')

# 참일때만 출력이 되서 else로 넘어감
if False:             
    print('거짓')  # true일때 실행
else:
    print('거짓말쟁이')  # false일때 실행

#%% none
## None(NULL)은 참도 거짓도 아님 None None이다

a = None

if a == False:             
    print('거짓')  # true일때 실행
elif a == True:
    print('참')  # false일때 실행
else:
    print("넌 먼데 \n None인데요 \n넌 머냐고 \n None이라고요;")
    

#%% if_참 거짓대신에 숫자넣어보기
# 권고하지 않음

# 0 은 거짓
money = 0
if money:
    print("참이다")
else:
    print("거짓이다")
    
# 0 이 아닌 숫자는 참
money2 = -1
if money2:
    print("참이다")
else:
    print("거짓이다") 
    
## 주의
if money2 == True:
    print("참이다")
elif money2 == False:
    print("거짓이다") 
else:
    print("==이라서 안됨")
#%%  if_문제
money = int(input('돈:'))
lunch = 6000
    
if money == lunch:
    print("점심 우마이!")
elif money > lunch:
    print(f'점심 우마이! \n 거스름돈:{money - lunch}원')
else:
    print(f'{lunch - money}원이 부족합니다')
    
    
#%% if_문제2
'''
[문제]
조건: 가진 돈의 가장 비싼 음료를 구매
1. 생수 1000
2. 콜라 2000
3. 사이다 3000
4. 커피 4000
''' 

my_money = int(input('돈:'))

if my_money >= 4000:
    print("coffee")
elif  my_money >= 3000:
    print("cyder")
elif my_money >= 2000:
    print("cola")
elif my_money >= 1000:
    print("water")
else:
    print("no money")
    
#%%   if_문제2_if안에 if
# 위문제에서 1000원 미만와 1000원 이상을 처리하고 음료구매


if my_money >= 1000:
    print("음료 구매가능")
    
    if my_money >= 4000:
        print("coffee")
    elif  my_money >= 3000:
        print("cyder")
    elif my_money >= 2000:
        print("cola")
    elif my_money >= 1000:
        print("water")
else:
    print("no money")
    
#%% in 사용

#해당하는 자료형에 x값을 가지고 있는가
a = [1,3,5,7,8]
x = 9
if x in a:
    print(f'리스트 {a}는 ({x})값을 가지고 있다.')
else: 
    print(f'리스트 {a}는 ({x})값이 없다.')

#%% 조건부 연산자(conditional expression)
# 변수 = 참 if 조건 else 거짓
# 굳이 쓸 이유는 없을거같음  if elif else쓰는게 더 편한듯

x = 10
y = True if x >= 10 else False   # java에서는 boolean z = (x >=10) ? true : false;
z = True if x == 0 else False

print(f'y는 x가 10보다 클때 True. x는 {x} 따라서 y는 {y}')
print(f'z는 x가 0 일때 True. x는 {x} 따라서 z는 {z}')

## y = True if x >= 10 else False를 if문으로 풀면
if x >= 10:
    z = True
else:
    z = False

#%%
'''
[문제]
점수에 따른 등급을 부여한다.
조건:
    점수의 범위는 0점에서 100점 사이여야한다
    범위를 넘어서면 "잘못됨 점수"라고 출력한다.
A: 90점 이상
B: 80점 이상
C: 70점 이상
D: 60점 이상
E: 60점 미만
# 일반 if 사용
# 조건부연산자 사용
'''

grade = int(input('점수: '))
# 일반
if grade >=0 and grade <= 100:
    if grade >= 90:
        print("A")
    elif grade >= 80 :
        print("B")
    elif grade >= 70 :
        print("C")
    elif grade >= 60 :
        print("D")
    elif grade < 60 :
        print("E")
else:
    print("잘못됨 점수")
#%%
# 조건부 연산자 사용
score = int(input('점수: '))

grade = 'A' if score >= 90 and score <= 100 \
    else 'B' if score >= 80 and score < 90 \
    else 'C' if score >= 70 and score < 80 \
    else 'D' if score >= 60 and score < 70 \
    else 'E' if score >= 0 and score < 60 \
    else "잘못된 점수"

print(grade)
#%% while
'''
## 반복문: while
## 특징:
    조건문이 참인 동안 while문에 속한 문장을 반복해서 실행한다
        => break로 무한 loop를 빠져나오거나 조건에 끝을 줘야됨
'''
# while_syntax

i = 0

while i <= 10:
    print(f'현재 i는 {i}입니다.')
    i = i + 1 

#%% 
last = 10
i = 0
s = 0

while i < last:
    i = i + 1
    s = s + i
    print(f'과정 i는 {i} 합(s)는 {s}')
print(s)


#%% while_break 
last = 5  # 탈출조건
i = 0
while True:    # 계속 참이라 break를 써서 끝내줘야됨
    # 종류 조건을 넣고 탈출
    if i == last:
        break    
    i = i + 1
    print(i)
    
#%% while_continue 
# 아래 있는 코드를 건너뛰고 맨 처음으로 돌아간다

i = 0
while i < 10:
    i = i +1
    if i == 3:
        continue   # 3이 나오면은 밑에 print를 안하고 위로 올라감
    print(i)

#%%
# [문제] while을 이용해서 1~100까지 연속된 수에서 홀수의 합을 구해라

i = 0
s = 0 
while True:
    if i >= 100:
        break
    i = i + 1
    if i % 2 == 1:
        s = s + i

    print(f'i = {i} s = {s} ')
    
print(s)

# 1부터 100까지 홀수의합
a = 1
b = 0
while True:
    b = b + a
    a = a + 2
    if a > 100:
        print(b)
        break
#%%
# [문제2] while을 이용해서 1~100까지 연속된 수에서 짝수의 합을 구해라

i = 0
s = 0 
while True:
    if i >= 100:
        break
    i = i + 1
    if i % 2 == 0:
        s = s + i
    print(f'i = {i} s = {s} ')
    
print(s)

# 1부터 100까지 짝수의합
a = 0
b = 0
while True:
    b = b + a
    a = a + 2
    if a > 100:
        print(b)
        break
    
#%%
# [문제] 정기 예금 복리계산
# 원금 10만원, 이자가 연 10%, 만기 10년, 복리로 계산하라

money = 100000
interest = .1
year = 1

while year <= 10:
    money = money + money * interest
    # 돈이니까 정수로
    print("(%d)년차 금액 (%d)  이자(%d)" % (year, money, money - 100000))
    year = year + 1
    
    
#%% 반복문: for  
'''
for 변수 in 리스트(또는 튜플, 문자열):
    수핼할 문장
'''
    
# 리스트 사용
li = [1,3,5,7,9]

# 리스트에 있는거 하나씩 꺼내기
for i in li:
    print(i)
    
# 튜플
t1 = (1, 3, 5, 7, 9)

for item in t1:
    print(item)

# 문자열
for item in "Hello, World":
    print(item)

#%% for_list 사용예제

score=[50, 60, 80, 90, 20]

a = 0
for i in score:
    a = a + 1
    if i >= 70:
        print(f'{a}번학생은 {i}점으로 합격입니다')
    else:
        print(f'{a}번 불합격')
        

#%% for_range사용

# range는 마지막숫자는 포함안함
for i in range(1, 11):   # 1~10까지
    print(i)
    
for i in range(11):  # 0~10까지
    print(i)
    
for i in range(0, 11, 2):  # 0~10까지 2칸씩 띄고
    print(i)               # 2 4 6 8 10 

#%%
# 위 예제에 range 적용
     # 0   1   2   3   4
score=[50, 60, 80, 90, 20]

# score[0]부터 차례대로 꺼내져서 for문이 돌아감
for i in range(len(score)):  
    if score[i] >= 70:
        print(f'{i}번학생은 {score[i]}점으로 합격입니다')
    else:
        print(f'{i}번 불합격')

#%%
sum = 0
for n in range(11):
    if n % 2 == 0:
        sum = sum + n
print(sum)

#%% 
# 구구단
for i in range(2, 10):
    print(f'{i}단')
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')
    print("")

#%% 
# [문제] for문을 사용해 9칸 짜리 피라미드를 그려라

# 날먹
for i in range(10):
    if i % 2 == 1:
        a = '*'* i    
        print("{0:^9}".format(a))   # 9칸 확보후 a 를 입력하고 가운데 정렬 
        
        
#%%
# 정석
a = "@"  # " "으로 바꾸면 완성
b = "*"
for i in range(1, 6):
    print(f"{a * (5-i)}{b * (2*i-1)}")



