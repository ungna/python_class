# dict : 사전형
# 키와 값을 한 쌍으로 선언
# { 키:값, ....}
# 특징 :
#   1. 검색(탐색) 속도가 빠른다.
#   2. 처리 용량을 많이 차지 한다.
#   3. 순차 검색 속도가 느리다.    
# 키는 변하는 않는 값을 사용해야 한다.
#   1. 리스트는 사용할 수 없다.
#   2. 튜플은 사용할 수 있다.

#%%

dt = {
      "title" : "파이썬의 이해",
      "author": "파이썬",
      "content" : "파이썬은 자유롭다."
}

print(dt)

#%%

# 키 목로(키 전체 리스트)
dk = dt.keys()
print(dk, type(dk), len(dk)) # <class 'dict_keys'>

lk = list(dk)   # dict_keys -> list
tk = tuple(dk)  # dict_keys -> tuple

print('리스트 형태:', lk)
print('  튜플 형테:', tk)

#%%

# 딕셔너리의 맨 마지막 요소의 값을 변경
dt[ lk[-1] ] = "파이썬의 세계"
print(dt)


#%%

# 딕셔너리의 값의 목록을 알고 얻음
vals = list(dt.values())
print(vals, type(vals))


#%%

# 딕셔너리 지우기
dt.clear()
print(dt)

    

