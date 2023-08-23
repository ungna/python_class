# format: 문자열 중간 중간에 특정 변수의 값을 넣어주기 위해서 사용
# 문자열 포맷 코드
# %s : 문자열(string)
# %c : 문자 1개(character)
# %d : 정수(decimal)
# %f : 실수,부동소수(float)
# {0} .format 

# %s : 문자열(string)
name = '한준희'
strformat = "오늘 당직자는 %s님입니다" % name
print(strformat)

#%% format 
# %d : 정수(decimal)
num = 30
numformat = "오늘의 온도는 %d도 입니다" % num
print(numformat)

# 부동 소숫점(%f) : float
eco = 3.45
print("올해의 한국 경제 성장율 예상치는 (%d) 입니다." % eco) # 결과: 3
print("올해의 한국 경제 성장율 예상치는 (%f) 입니다." % eco) # 결과: 3.450000

#%% format 
# %c : 문자 1개(character)
# %c를 쓰면은 숫자는 기본적으로 ASCII로 인식하는거같음
ch1 = 65  #ASCII, 대문자('A')
ch2 = 'A'
ch3 = 'a'
ch4 = 97  #ASCII, 소문자('a')
print("%c %c %c %c는 하나의 문자입니다." % (ch1, ch2, ch3, ch4))

ch1 = 65 # 영문자는 ASCII, 대문자('A')
print (" ASCII Code (%d)는 (%c) 입니다." % (65, 65))

#%% format 
# 문자열과 정수를 복합적으로 써서 문자열 포매팅에 적용할 때
# 대응되는 값 또는 리스트는 % (a, b)로 묶어야 한다.

today = "2023-08-23"
temp = 30
msg = "오늘의 날짜는 %s이며, 온도는 %d도 입니다." % (today, temp)
print(msg)

#%% format_정렬
# %숫자d : 숫자만큼 자릿수를 확보하여 출력하고 남는 부분은 공백으로 출력
# 정렬: 기본 오른쪽 맞춤
# 왼쪽정렬 : %-숫자d
a = 12
b = 1234
c = 1234567
print("오른쪽 정렬")
print("a는 (%6d)입니다." % a)
print("b는 (%6d)입니다." % b)
print("c는 (%6d)입니다." % c)  #할당한 칸보다 큰값이 들어오면 값이 우선

print("왼쪽정렬")
print("a는 (%-6d)입니다." % a)
print("b는 (%-6d)입니다." % b)
print("c는 (%-6d)입니다." % c)

#%% format_정렬 소수
# 소수점 : 소수점도 전체 자릿수에 포함
pi = 3.14
print("원주율은 (%f)입니다." % pi)  # float의 기본은 소수점이하 6칸
print("원주율은 (%10f)입니다." % pi) # 소수점 6칸을 확보하고 나머지 2칸 공백
print("원주율은 (%10.2f)입니다." % pi)  # 소수점을 설정해서 공백이 많아짐
print("원주율은 (%-10.2f)입니다." % pi)  # 왼쪽정렬에 소수점2자리 나머지 공백
print("원주율은 (%10.0f)입니다." % pi)  # 소수점 이하 짜름

#%% format_정렬 소수
num = 1234.12345
print("원주율은 (%4.2f)입니다." % num)  
print("원주율은 (%1.2f)입니다." % num)  # 전체칸이 모자라도 앞에 정수부분까지는 입력됨

#%% format_{}

# {0} .format 
# 자료형은 알아서 변환을 시킨다.
num = 30
numformat = "현재 온도는 {0}도 입니다.".format(num)
print(numformat)

name = '한준희'
strformat = "오늘 당직자는 {0}님입니다" .format(name)
print(strformat)

#%% format_{}
msg = "나는 {0}, 너는 {1}, 쟤는 {2}.".format('1등', '2등', '3등')
print(type(msg), msg)  # type은 str

msg2 = "나는 {2}, 너는 {0}, 쟤는 {1}.".format('1등', '2등', '3등')
print(msg2)  # ()안에 숫자는 .format안에 순서

#%% format_{}
# 이름으로 넣기 : 파라미터 이름(인자이름)
msgfmt = "오늘의 날짜는 ({today})이며, 온도는 ({temp})도 입니다."
print("이름으로:", msgfmt.format(today='2021-12-28', temp=30))

# 연산식을 넣을 수 있다.
# temp + 2
msg = f"내일의 온도는 ({temp + 2})도 입니다."
print(msg)


#%% format_{}_정렬

a = 12
b = 1234

# 전체 자릿수 5자리를 확보하고 왼쪽 정렬
# {순번:공백대체문자<자릿수}
print("[전체 자릿수 5자리를 확보하고 왼쪽 정렬]")
print("a의 포인트는 ({0:<5})입니다.".format(a))
print("b의 포인트는 ({0:<5})입니다.".format(b))

# 전체 자릿수 10자리를 확보하고 오른쪽 정렬
# {순번:>자릿수}
print("[전체 자릿수 5자리를 확보하고 왼쪽 정렬]")
print("a의 포인트는 ({0:>5})입니다.".format(a))
print("b의 포인트는 ({0:>5})입니다.".format(b))


# 전체 자릿수 10자리를 확보하고 가운데 정렬
# {순번:^자릿수}
print("[전체 자릿수 5자리를 확보하고 가운데 정렬]")
print("a의 포인트는 ({0:^6})입니다.".format(a))
print("b의 포인트는 ({0:^6})입니다.".format(b))

#%% format_{}_정렬
# 공백대체문자
# {순번:공백대체문자<자릿수}

print("a의 포인트는 ({0:.>5})입니다.".format(a))
print("b의 포인트는 ({0:->5})입니다.".format(b))
print("a의 포인트는 ({0:=<5})입니다.".format(a))
print("b의 포인트는 ({0:@<5})입니다.".format(b))


#%% format_f"{변수}"
a = '나는'
b = 'mk-'
c = 1234

print(f"{a} {b}{c}")


d = f"{a} {b}{c}"
print("자기소개해봐.", d, "로봇이죠")


#%% format_f"{변수}"_정렬
a = 1

# 왼쪽정렬
print(f"포인트 목록:({a:<5})")
# 오른쪽정렬
print(f"포인트 목록:({a:>5})")
# 가운데정렬
print(f"포인트 목록:({a:^5})")

#%% format_f"{변수}"_input응용
a = input('')
print("지금 로아 골드값은", a ,":100")


#%% count
# 문자 개수 세기(count)
# 숫자는 사용x 
# 문자열에서 특정한 문자를 몇 개를 포함하고 있는가?
a = 'hobby'
print('count=', a.count('b'))
print('count=', a.count('B'))  # 대소문자 따짐

# 숫자는 count() 메소드를 가지고 있지 않음 = 숫자는 안됨
# SyntaxError: invalid syntax
# num = 1007
# numcount = 1007.count('0')

#%% count_응용
b = 'welcome to Korea'
print(f"{b}.count(' ') = {b.count(' ')}")  # f""를 쓰면은 {}안에 함수넣어야써짐

tel = "010-3938-0732"
telcount = tel.count('-')
print(f"전화번호 {tel}에는 하이픈이 {telcount}개 있습니다.")

#%% find
# 문자열 위치 검색(find)
# 최초 만나는 문자열 위치를 찾음

#    0123456789012345678901234
a = "Python is the best choice"
a1 = a.find('i')
a2 = a.find('k')

print('i=', a1)
print('k=', a2)   # 찾지못하면은 -1 리턴

print('is=', a.find('is'))

#%% find_연속해서 찾는법_쓰레기
# 슬라이싱

# 0123456789012345678901234
# Python is the best choice
a = "Python is the best choice"
first = a.find('t')
print('first t = ', first)
a_cut = a[first+1:] # 처음 t에서 짜르고 뒷부분을 a_cut에 넣음
                    # 뒷분을 복제해야되서 별로 효율적이지 않음
print(a_cut)
second = a_cut.find('t')
print('first t = ', first)
print('second t = ', first+second+1)  # 짜른부분 + 두번쨰 위치 + a_cut에서 한 +1 


#%% find_연속해서 찾는법_좋은방법
# 문자열.find(검색문자열, 시작위치)
# string.find(findstring, startindex)
print(f"문자열 {a}에서 문자't'의 위치 검색")
first = a.find('t')
print('first t =', first)

second = a.find('t', first + 1)
print('second t =', second)


#%% join 
# 각 문자들 사이에 문자열을 삽입한다.
# '사이에 넣을거'.join(원본)
s1 = ','.join('abcde')
print(s1)

s2 = ','.join('가나다(abc)')
print(s2)

s3 = 'tlqksusdk'
print('!'.join(s3))

#%% join_list에 삽입

ls= ['A', 'B', 'C', 'D']
s1 = ', '.join(ls)
print(ls)
print(s1)

s2 = '님 어서오세요 \n'.join(ls)
print(s2)    # 사이에 넣는거라 마지막꺼에는 적용안됨 ㅠ
print('--------')
print(s2 +'님 어서오세요') # 마지막꺼에 수동으로 넣어줌


#%% upper_lowwer
# 문자열을 대 소문자로 변환시켜줌
# 원본은 변경되지 않는다.

A = 'LOSTARK'
a = A.lower()
print(a)

b = 'goldriver'
B = b.upper()
print(B)

# 영문이 아닌 경우 + 이미 대,소문자인 경우는 그대로 출력
Hangeul = "한글과 EngLish"
print(Hangeul, "->", Hangeul.upper())
print(Hangeul, "->", Hangeul.lower())

# 원본 그대로인거 확인
A = 'LOSTARK'
print(A.lower())
print(A)

#%% strip(공백제거)

a = '          hi          '
nospace_a = a.strip()
print(f"({nospace_a})")

# left \-strip
a = '          hi          '
noleft_a = a.lstrip()
print(f"({noleft_a})")

# right-strip
a = '          hi          '
noright_a = a.rstrip()
print(f"({noright_a})")

#%% replace
# 문자열에서 바꾸고자 하는 문자열을 찾아서 새로운 문자열로 대체
# 새로운문자열 = 원본문자열.replace(대상문자열, 새로운문자열)
# 원본은 변경되지 않는다.

a = 'Life is too short!'
b = a.replace('Life', 'Your leg')
print(f"{a} -> {b}")

# 대소문자를 구분한다.
a = 'Life is too short!'
b = a.replace('life', 'Your leg')
print(f"{a} -> {b}")  # 바꾸고자 하는 문자열이 없으면 안바꿔짐

#%% replace_응용

# String.capitalize() : 첫번째 문자를 대문자로 변환해서 변환된 문자열을 리턴
s = 'life'.capitalize() 
print('s=', s)
c = a.replace(s, 'Your leg')
print(f"({a}) -> ({c})")



#%% split
# 공백을 기준으로 문자열을 분할하여 배열(list)형으로 리턴
a = 'Life is too short!'
b = a.split()
print(b)

# 다시 문자열로 변환
c = ' '.join(b)
print(c)



