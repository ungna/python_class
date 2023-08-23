# 집합: set
# 합집합, 교집합, 차집합
# 특징 :
#    1. 중복을 허용하지 않음
#    2. 순서가 없다.

#%%

# 빈 셋
s = set()    
print(s, type(s))
# set() <class 'set'>

#%% 
weeks = { 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' }
print(weeks, type(weeks))
# {'Mon', 'Sat', 'Thu', 'Fri', 'Sun', 'Tue', 'Wed'} <class 'set'>

#%%

# 문자열을 셋으로 선언
alpha = set("ABCDEFG")
print(alpha)
