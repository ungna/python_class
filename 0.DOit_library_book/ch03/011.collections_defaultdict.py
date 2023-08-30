# 딕셔너리를 한번에 초기화하려면?
# collections.defaultdict: 값에 초깃값을 지정하여 딕셔너리를 생성
# https://docs.python.org/ko/3/library/collections.html

from collections import defaultdict


text = "Life is too short, You need python"

# defaultdict생성
d = defaultdict(int)

# 사용한 문자를 key로 사용횟수를 value로 만들어서 딕셔너리에 넣기
for c in text:
    d[c] += 1

print(dict(d))


#%%

# defaultdict생성 없으면
# 키값이 없는 상태에서 += 연산을 수행해서 KeyError: 'L' 에러가뜸 
# 에러가 안뜨려면은 #으로 막아준것을 해서 초기값을 잡아줘야됨
d = dict()
for key in text:
#    if key not in d:
#        d[key] = 0
    d[key] += 1

print(d)








