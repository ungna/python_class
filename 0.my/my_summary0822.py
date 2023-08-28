# operator  연산자

# 더하기
a = 10
b = 20
c = a+b
print('a+b =' , c)

# 빼기(-)
d = b-a
print('b-a =' , d)

#%%
# 곱하기(*)
a = 2
b = 3
c = 4
d = a * b * c
print('a x b x c = ', d)

# 지수(제곱)(**)
# 10의 3승(10 * 10 * 10)
a = 10
b = 3
c = a ** b
print('c=', c)

#%%
# 나누기(/)
a = 10
b = 3
c = a / b
print('c = b / a :', c)   # 소수점까지 다 포함

# 나누고 몫만 가지기 (//)
a = 10
b = 3
c = a // b
print('c = b // a :', c)   # 소수를 버리고 몫만 나옴

# 나누고 나머지만 가지기 (%)
a = 10
b = 3
c = a % b
print('c = b % a :', c)

# 몫 나머지 둘다 표시 (divmod)
# (몫, 나머지)   이렇게 표시됨
a = 10
b = 3
g = divmod(a, b)
print(g)
print('몫:', g[0])         # 인덱스로 표시
print('나머지:', g[1])

#%% 복합 대입연산자
# 더해서 대입 +=
a = 10

a += 10 # a = a + 10
print(a)


#%% 연산자 우선순위  like 일반 수학
# 곱셈과 나눗셈은 우선순위가 같다.
# 덧셈과 뺄셈도 우선순위가 같다.
# 같은 우선순위에서는 왼쪽에서 오른쪽 계산하면서 간다. 

a = 10
b = 20
c = 2

# (곱셈, 나눗셈) -> (덧셈, 뺄셈)
d = a + b * c
print('d=', d) # 60(X) or 50(O)


# 덧셈을 곱셈보다 먼저 연산을 수행하게 하려면?
d = (a + b) * c
print('d=', d)

#%%print() 함수 사이에 넣기 sep
print('hi', 'hello')
print('hi', 'hello', sep='!!' )

# enter없이 
print('asd', end='') # 라인피드(Enter) 키를 없앰
print('가나다', end='') 

#%% escape
# 백슬래시(\) 기호를 사용
# 키보드에서 Enter 키를 치면 내부에 입력되는 코드(\n)
print("one\ntwo\nthree")

# 탭(Tab) : \t
print("one\ttwo\tthree\t1234567890123\tABC")

# 기타 특수문자에 \를 사용해서 출력
msg = "영희는 철수에게 \"안녕\"이라고 말했다."
msg2 = "He is always saying \\Could you say is again?\\"

print(msg)
print(msg2)


#%% Str
# 문자열은 데이터로서 문자들의 집합
# "" 또는 ''  둘다 사용가능
helloworld = "hello world"
print(helloworld)

helloworld2 = 'hello, world'
print(helloworld2)

# 가장 바깥을 작은 따옴표로 감싸서 문자열로 처리하고
# 안쪽의 큰 따옴표는 문자 자체로서 출력된다.
hellopython2 = '"파이썬"은 오늘날 가장 인기있는 언어로서 "빅데이터"처리와 "인공지능"에서 사용된다.'
print(hellopython2)

#%% 다중라인
# 문자열이 다중 라인인 경우 인용부호가 겹쳐도 된다.
print("[큰 따옴표로 선언한 다중라인 문자열]")
hello = """안녕하세요?
"파이썬"의 세계에
오신 것을 환영합니다."""
print(hello)

# 다중라인을 만들었지만 \을 사용해 다시 한줄로 만들 수 있음
hello = "안녕하세요? \
'파이썬'의 세계에 \
오신 것을 환영합니다."
print(hello)

#%%  indexing_문자열 인덱싱
s = "abcdefghijklmnopqrstuvwxyz" # 26자
ln = len(s)


print('len(s):', ln)  #26
# 코딩에서는 숫자가 0부터 시작해서 길이는 26이지만 z는 25번쨰에 있음
print(s[0])     #a
print(s[25])    #z
print('s[len(s) - 1] = ', s[len(s) - 1]) # z

#%% 문자열 인덱싱_음수
# 음수로 시작하면은 뒤에서 부터 새는데 처음이 -1이다
print(s[-1])    # z 
print(s[-26])   # a

#%% slicing
# 문자열의 위치를 참조를 통해서 특정한 범위의 문자열을 추출
s = "0123456789"
print(s)

# 문자열[시작번호:끝번호]
# 시작번호:끝번호(3~6)  
a = s[3:7]    # 끝번호는 적용안함 like 미만  => len이랑 같이 사용하면 편함
print(a)


a = s[:10]  # 처음부터 10미만까지
a = s[5:]   # 5부터 끝까지
a = s[:] # 처음부터 끝까지


#%% slicing_len사용
# len
s = "0123456789"
t = len(s)     # len을 쓰면은 1부터 새서 하나 더 크게 나오지만 
a = s[:t]      # slicing에서 끝번호는 적용 안해서 오히려 좋음

print(a)

#%% slicing_음수 
print(s[-1:])  # 제일 뒤에서 끝까지 추출  #9
print(s[-4:])  # 6789
      
#%% slicing_건너뛰기

s = "0123456789"
# 문자열[시작번호:끝번호:스텝]
print(s[0:7:2]) # 0246


# 홀수만
odd = s[1::2]
print(odd)

# 짝수만
even = s[1::2]
print(even)
