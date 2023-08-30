# re(regular expressions): 복잡한 문자열을 처리할때 사용하는 기법
# re 공식문서: https://docs.python.org/ko/3/library/re.html

import re
# match
# search


#%% 
# match  vs search
# match는 처음 시작하는 부분이 일치하는지 확인하고 그 단어를 줌
# search는 어느 위치에 있던 처음만난거를 찾음
# match든 search든 하나만 찾지만 여러개 찾으려면 findall을 써야됨 - 010.collections.Counter 에서 사용한 예제있음

p = re.compile("[a-z]+") 

print(p.search("hello"))       # <re.Match object; span=(0, 5), match='hello'>
print(p.search("Hello world"))  # <re.Match object; span=(1, 5), match='ello'>
print(p.search("HELLO world"))   # <re.Match object; span=(6, 11), match='world'>

#%%

data = '''
[2023-08-29 10:15:009] [WARN] 통신장비 통신 장애 발생
'''


# 날짜패턴   
p = re.compile("[0-9]+[-]+[0-9]+[-]+[0-9]+") 
# p = re.compile("[0-9-]+")              # 이렇게도 가능
# p = re.compile("\d{4}-\d{2}-\d{2}")    # 이렇게도 가능


# 날짜가 -가 아니라 / . 으로 해도 되게
# p = re.compile("[0-9]+[-./][0-9]+[-./][0-9]+")


# data에서 날짜패턴 추출
data_compile = p.search(data)

# 추출한거 출력
if data_compile != None:
    sp, ep = data_compile.span()  # data_compile.span()의 시작위치 마지막위치를 sp ep에 넣음
    print("추출한 날짜:", data[sp:ep])
else:
    print("None떳음")

# 날먹출력
print("-" * 10)
print(data_compile)



#%%
# [] 안에있는거 출력
data = '''
[2023-08-29 10:15:009] [WARN] 통신장비 통신 장애 발생
'''

# [] 위치 특정
p1 = re.compile("\[")
p2 = re.compile("\]")

# [] or ()
# p1 = re.compile("\[|\(")   # [ or (
# p2 = re.compile("\]|\)")   # ] or )

data_compile1 = p1.search(data)
data_compile2 = p2.search(data)

# 위치 추출
sp = data_compile1.span()[0]
ep = data_compile2.span()[1]

# [] 안에있는거 출력
print("날짜: ", data[sp: ep])


#%%

data = '''
[2023-08-29] [10:15:009] [WARN] 통신장비 통신 장애 발생
'''

p = re.compile("\[(\d{4}|\d{2})[-]\d{2}[-]\d{2}\]") 
# 일자: 대괄호[]로 감싸 있어야 한다  =>  \\[     \\]
# 년: 2자리 또는 4자리     => (\d{4}|\d{2})
# 월: 2자리               =>  \d{2} 
# 일: 2자리               =>  \d{2} 

# data에서 날짜패턴 추출
data_compile = p.search(data)


# 추출한거 출력
if data_compile != None:
    sp, ep = data_compile.span()  
    print("추출한 날짜:", data[sp:ep])
else:
    print("None떳음")
