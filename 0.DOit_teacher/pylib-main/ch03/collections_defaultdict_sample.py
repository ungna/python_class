
# 딕셔너리를 한 번에 초기화

from collections import defaultdict

# 문자열의 각 문자를 딕셔너리의 키로하여
# 각 문자의 발생 횟수를 빈도수 값으로 지정
text = "Life is too short, You need python."


#%%

# d = dict()
d1 = {}
for key in text:
    if key not in d1:
        d1[key] = 0
    d1[key] += 1
    
print(d1, type(d1))    
print("-" * 50)

#%%

# 0으로 초기화
dd = defaultdict(int)

# <class 'collections.defaultdict'> defaultdict(<class 'int'>, {})
print(type(dd), dd) 

# 참조해서 해당하는 키가 없으면
# 키에 해당하는 키를 생성하고 값은 0으로 초기화
for c in text:
    # dd[c] = dd[c] + 1
    dd[c] += 1 

print(dict(dd))
