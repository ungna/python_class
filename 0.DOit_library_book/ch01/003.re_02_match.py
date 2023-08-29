# re(regular expressions): 복잡한 문자열을 처리할때 사용하는 기법
# re 공식문서: https://docs.python.org/ko/3/library/re.html

import re
# match

# 반드시 알파벳으로 시작
# 문자열의 처음이 소문자 a부터 z까지의 임의문자가 1번이상 나오는 패턴
p = re.compile("[a-z]+") 

print(p.match("Hello"))  # None이 나옴   H로 시작해서

print(p.match("hello")) # <re.Match object; span=(0, 5), match='hello'>
                          # span()  : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

#%%
# span에는 조건에 해당하는 단어의 길이가 나옴
# match에는 조건에 해당하는 단어가 나옴
print(p.match("hello, world"))  # <re.Match object; span=(0, 5), match='hello'>
print(p.match("helloworld"))   # <re.Match object; span=(0, 10), match='helloworld'>

# 문자열의 처음부터 찾음 중간부터는 안됨
print(p.match("Hello world"))  # None     H로 시작해서
print(p.match(" hello world"))   # None   공백으로 시작해서

#%%
p = re.compile("[a-z]+")

# p = re.compile("[a-zA-Z]+")  # 대소문자 전부  
# 띄어쓰기나 , 같은거 쓰면 그거까지인식하는거라 걍 다 붙혀서 써야됨

s = "hello world"
m = p.match(s)

if m != None:
    print('m.span:', m.span(), type(m.span()))
    sp, ep = m.span()  # m.span()의 시작위치 마지막위치를 sp ep에 넣음
    print("매치된 문자열:", s[sp:ep])  # s에서 시작위치 마지막위치를 슬라이싱해서 단어를 찾음
else:
    print("None떳음")

#%%
# 컴파일 좀더 알아보기

# +가 없으면은 뒤에 단어는 포함안하고 알파벳 하나만 찾음
x = re.compile("[a-z]")   
print(x.match("hello world"))     # <re.Match object; span=(0, 1), match='h'>

# \s : 띄어쓰기  즉 단어에 띄어쓰기 한거까지 포함
s = re.compile("[a-z]+\s")
print(s.match("hello world"))  # <re.Match object; span=(0, 6), match='hello '>

# 띄어쓰기 2개
s2 = re.compile("[a-z]+\s{2}")
print(s2.match("hello world"))  # None  




