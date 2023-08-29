# re(regular expressions): 복잡한 문자열을 처리할때 사용하는 기법
# re 공식문서: https://docs.python.org/ko/3/library/re.html

import re

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

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

