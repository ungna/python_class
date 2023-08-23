# 주석: 실행과 관련없는 설명문
print("Hello")

# if
a = 4
if a == 4 :
    print("good")


# def 
def printx(x):
    print('[printx]')
    print('[' + x + ']')

def printy(x):
    print('[printx]', end='')
    print('[' + x + ']')

printx("Hello x")
printy("Hello y")


#abc  # 초기값 설정 안하면 오류남
abc = 123

#세미콜론 써도되고 안써도됨
print("난 세미콜론 있음");
print("난 그런거 안씀")

#%%  var
# spyder에서 위에서 쓴걸로 cell 구분
#한글로 변수 선언가능
홍길동 = '나는 홍길동'
전우치 = '나는 전우치'
전우치 = 홍길동    # 원래값은 덮어씌어짐
print(전우치)

홍길동 = 11111   #다른 자료형으로 변경가능
print(홍길동)   


# 구분자 사용
print(전우치, 홍길동)  # 구분자 사용 안하면 다음줄로 안넘어가고 쭉한줄로
print(전우치, 홍길동, sep = ',')
print(전우치, 홍길동, sep = ', ')
print(전우치, 홍길동, sep = '/ ')

# 따로 출력해도 다음 라인으로 이동하지 않고 연속해서 출력
print(전우치, end='')
print(홍길동, end= '')
print("이게뭐야")

#%%  var_2
# 한라인에 여러개 선언
a, b, c = (3, 5, 7)
print('a=', a)
print('b=', b)
print('c=', c)

# x와 y의 값을 바꾸려면?
x = 77
y = 88

print('x와 y값의 교환')
z = x   # x값을 z에 임시보관(대피)
x = y
y = z
print('x=', x)
print('y=', y)

# 파이썬에서는 이걸 한라인으로 구현가능
x = 77
y = 88

print('한줄로 x와 y값의 교환')
x, y = y, x
print('x=', x)
print('y=', y)

#%% int
# 정수: 0, 1234, -1234, 소숫점이 없는 값(유리수)

print(type(1234))
print(type('1234'))  #숫자이더라도 ''안에 넣으면 str로 표시

a = 14 
b = 3

# 나머지만 출력
print("나머지만: ", a % b )
# 몫만 출력
print("몫만: ", a // b ) 

#%%  input

#input()
#키보드로 내용을 입력
abc = input('값을 입력하게요: ')

print(abc)
print(type(abc))        #기본으로 input()함수가 리턴하는 자료형은 문자열
 
num = int(abc)        # int()로 자료형을 변환
print(num, type(num))

#TypeError: can only concatenate str (not "int") to str
#문자열과 숫자 연산오류(+, -)
two = abc + num

#문자열끼리는 가능
p1 = '010 '
p2 = '1111 '
p3 = '2222'
phone = p1 + p2 + p3
print(phone)

#곱하기는 오류안남  문자열을 숫자번 만큼 반복해서 쓰라는 뜻 
three = abc * num
print("곱하기 사용: ", three)  

#%%  str
# 멀티라인 주석
"""
멀티라인 주석
multi-line comment
멀티라인 주석
multi-line comment
"""
# 주석말고 문자열을 여러줄로 묶을떄도 사용
multi_String = """
aaaaaaa
bbbbbbb
ccccccc
ddddddd
"""
#\n사용
oneline_String = "aaaaaaa\nbbbbbbb\nccccccc\nddddddd"

#\t사용
tabline_String = "aaaaaaa\tbbbbbbb\tccccccc\tddddddd"

print("multi_String: ", multi_String)
print("oneline_String: ", oneline_String)
print("tabline_String: ", tabline_String)

##/n /t는 문자열이라 ''안에 넣어서 써야됨
print(oneline_String + '\n\n' + tabline_String)


# 문자열에 큰 따움표 사용하기
easy = '"Python is very easy" he said'   #다른 종류의 따움표 사용
hard = "\"Python is hard\" I replied"    #역슬래시 사용

print(easy)
print(hard)


#%%  str -  \t 추가설명
# \t
# \t 으로 8칸씩 확보 확보한칸을 다쓰면 새로 8칸확보(spider는 8칸)
print("0123456789"*3)
print("a\tb\tc")
print("abc\tb\tc")
print("abcd\tb\tc")
print("abcdefghi\tb\tc")
print("abcdefg  \tb\tc")

#%% bool
## True 또는 False

#결과는 book자료형
a = (1 == 1)
b = (1 != 1)
c = (a == b)
d = (a != b)
s= ('홍길동' == '홍길동')
x = (d != s)

print('a: ', a, type(a))  #T
print('b: ', b, type(b))  #F
print('c: ', c, type(c))  #F
print('d: ', d, type(d))  #T
print('s: ', s, type(s))  #T
print('x: ', x, type(x))  #F

#%% bool_2
## <  >  <=  >=  and  or  not 등등 사용
## True = 1   False = 0
## is : == 단, 변수끼리만 사용가능
a = (1 > 2)
b = (1 < 2)
c = (True > False)  # 1 > 0
d = (True < False)  # 1 < 0
s = (a is b)        # F == T

print('a: ', a, type(a))  #F
print('b: ', b, type(b))  #T
print('c: ', c, type(c))  #T
print('d: ', d, type(d))  #F
print('s: ', s, type(s))  #F

#%% float
a = 1
b = 1.0
c = (a == b)    #T
#javascript에서만 사용하는거 ===
# d = (a === b)  type까지 같아야됨
# d = (type(a) == type(b))  # int == float   #F


print(c)
print(d)

#%% float_2 
# 10의 3승(10이 3번 곱해진 값) : 1000 == E3 == e3
# 4.24 * 10의 3승
# 값 4240.0
a = 4.24E3
b = 4.24 * 1000
print('a=', a)
print('b=', b)

# 0.123 * 10의 -3승
# 값 : 0.000123
c = 0.123E-3
print('c=', c)


#%% instance
# 자료형이 객체(object)화 된 상태 인스턴스
# 객체를 생성할 떄 메모리가 할당 될때 인스턴스
# 객체: 고유한 자료의 실체를 구별

# isinstance()는 인자로 전달된 객체가 type과 일치하는지 T F형식으로 나옴
f = 0.1234
print('f type:', type(f)) # float(실수형)
print('f fs instance:', isinstance(f, float))  # float float   # T

ft = type(f) # float
print('ft type:', type(f))
print('f ft instance:',isinstance(f, ft))   # float float   # T

fs = type(str(f))
print('fs type:', fs)  # str
print('int str instance:', isinstance(f, fs))  #float str    # F
print('int str instance:', isinstance(f, str))  #float str    # F


#%% 16진수 (hexa)- 숫자앞에 0x, 0X 표기   8진수 (octa) - 숫자앞에 0o 표기  2진수 (binary) - 숫자뒤에 (2) 표기
# 2진수  : 0 1 
# 8진수  : 0 1 2 3 4 5 6 7 
# 10진수 : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 16진수 : 0 1 2 3 4 5 6 7 8 9 a  b  c  d  e  f 

# 2진수 계산  1101(2)  =>  2^3 + 2^2 + 0*2^1 +2^0
# 8진수 계산  0o7532  =>  7*8^3 + 5*8^2 + 3*8^1 + 2*8^0
# 16진수 게산  0X2a3  => 2*16^2 + 10*16^1 + 3*16^0

# 1바이트로 최대 표현할 수 있는 값
# 16진수 : 4개의 비트가 한 단위로 구성
#  2진수: 1111 1111
# 16진수: 0xff
# 10진수: 255
#  8진수: 1바이트에 정확히 대응 x 

# 2바이트
#  2진수: 1111 1111 1111 1111
# 16진수: 0xffff
# 10진수 : 65535
#  8진수 : 0o177777
