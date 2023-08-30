# 사용한 단어 개수를 구하려면?
# collections.Counter: tuple은 인덱스를 통해서만 접근이 가능하지만
# nemadtuple은 인덱스 뿐 아니라 키로도 데이터에 접근하게 하는 자료형이다
# https://docs.python.org/ko/3/library/collections.html

from collections import Counter
import re

data = """
산에는 꽃 피네.
꽃이 피네.
갈 봄 여름없이
꽃이 피네.

산에
산에
피는 꽃은
저만치 혼자서 피어있네.

산에서 우는 새여
꽃이 좋아
산에서
사노라네.

산에는 꽃지네
꽃이 지네.
갈 봄 여름 없이
꽃이 지네.
"""

# findall 문법:  re.findall(r'패턴 문자열', '문자열')  # \w+: 문자만 뽑아낸거
words = re.findall(r'\w+', data)
counter = Counter(words)
print(counter.most_common(1))  # 빈도가 가장 높은거 1

#%% 
# 빈도가 2로 같을경우 같이 나온거 중에 가장 앞에있는거
print(counter.most_common(5))  # [('꽃이', 5), ('피네', 3), ('산에는', 2), ('갈', 2), ('봄', 2)]
print(counter.most_common(3))  # [('꽃이', 5), ('피네', 3), ('산에는', 2)] 
# '산에는' 이 시의 맨 앞에 있어서 '갈'이나 '봄'보다 먼저나옴

#%%
# words = re.findall(r'\w+', data) 파해치기 # 한번 해보기
# strip 으로 . ./ 제거
# split(' ') 으로 나누고 리스트형식으로 넣기
