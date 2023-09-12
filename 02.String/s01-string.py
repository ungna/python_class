# 문자열(String)
# 변수 이름과 구별되며 리터럴(literal)
# 문자열은 데이터로서 문자들의 집합
# 큰 따옴표(")로 감싸서 문자열이라는 것을 알린다.
# 작은 따옴표(')로 감싸서 문자열이라는 것을 알린다.

# 빈 문자열 생성
hello = ""
world = ''
print(f'hello=[{hello}]')
print(f'world=[{world}]')

helloworld = "hello world"
print(helloworld)

helloworld2 = 'hello, world'
print(helloworld2)

# 가장 바깥은 문자열이라는 것은 의미하고 
# 문자열 안에 있는 따옴표는 문자 자체로서 출력된다.
hellopython = "'파이썬'은 오늘날 가장 인기있는 언어로서 '빅데이터'처리와 '인공지능'에서 사용된다."
print(hellopython)

# 가장 바깥을 작은 따옴표로 감싸서 문자열로 처리하고
# 안쪽의 큰 따옴표는 문자 자체로서 출력된다.
hellopython2 = '"파이썬"은 오늘날 가장 인기있는 언어로서 "빅데이터"처리와 "인공지능"에서 사용된다.'
print(hellopython2)

""" 
문자열(String)
다중 라인의 문자열을 하나의 문자열로 선언
큰따옴표(")를 연속해서 3개로 감싼다.
작은따옴표(')를 연속해서 3개로 감싼다.
"""

# 큰따옴표
print("[큰 따옴표로 선언한 다중라인 문자열]")
hello = """안녕하세요?
'파이썬'의 세계에
오신 것을 환영합니다."""
print(hello)

# 작은따옴표
print("[작은 따옴표로 선언한 다중라인 문자열]")
hello = '''안녕하세요?
"파이썬"의 세계에
오신 것을 환영합니다.'''
print(hello)

# 큰따옴표
# 문자열이 다중 라인인 경우 인용부호가 겹쳐도 된다.
print("[큰 따옴표로 선언한 다중라인 문자열]")
hello = """안녕하세요?
"파이썬"의 세계에
오신 것을 환영합니다."""
print(hello)

# 문자열(String)
# 하나의 라인의 문자열을 백슬레시(\)를 써서 연결할 수 있다

hello1 = "안녕하세요? "
hello1 += "'파이썬'의 세계에 "
hello1 += "오신 것을 환영합니다."
print(hello1)

# 라인피드를 넣음 : new line(\n)
hello2 = "안녕하세요? \n"
hello2 += "'파이썬'의 세계에 \n"
hello2 += "오신 것을 환영합니다."
print(hello2)
