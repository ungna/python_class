# re(regular expressions): 복잡한 문자열을 처리할때 사용하는 기법
# re 공식문서: https://docs.python.org/ko/3/library/re.html

import re
#sub

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

# 라이브러리 사용안하고 일반 코드로 짜기
result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))



#%%
# 코드 분석

# 주민번호 검열해서 넣을 빈 문장 하나 넣을 리스트 만듬
result = []

# \n을 쓴거 기준으로 라인을 짜름
for line in data.split("\n"):
    # 라인별로 처리할거라 새로운 라인이 시작됨녀 리셋할 빈리스트를 만듬
    word_result = []

    # 띄어쓰기 기준으로 단어별로 짜름
    for word in line.split(" "):
            
        # len(word) == 14 주민번호 길이라 가운데 기호(-) 포함해서 14인걸로 주민번호를 찾음
        # 혹시 ㅈㄴ 긴단어가 있을수 있으 주민번호를 특정하기위해 앞에 6자번호 뒤에 7자번호로 and 써서 묶음 
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        
        # 검열 통과한 단어를 추가함 
        # 안바뀐거는 그대로 주민번호의 경우 겸열된게 추가됨
        word_result.append(word)
        
    # 처리한라인을 result에 합쳐서 하나의 문자열로 만듬
    result.append(" ".join(word_result))

# 합친 문자열 출력해서 결과 띄움
print("\n".join(result))


#%%

# 라이브러리 이용해서 짜기

                 # 숫자6 - 숫자7 과 같은 형식의 문자열을 특정해서 pat에 넣음
pat = re.compile("(\d{6})[-]\d{7}")

# pat를 sub 함수를 이용해 교체한다 
print(pat.sub("\g<1>-*******", data))

#%%
# 그룹핑
pat = re.compile("(\d{6})[-](\d{7})")

# g는 ()로 묶에 지정한 그룹 
# g<1>은 첫번째 그룹을 문자열에서 바꾸지 않고 그대로 사용한다는 뜻
print(pat.sub("\g<1>-*******", data))

print(pat.sub("\g<1>-\g<2>", data))
