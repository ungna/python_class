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

# 키를 가지고 값을 찾음
print(dt['title'])
print(dt['author'])
print(dt['content'])


#%%

# get() 메소드 
t1 = dt.get('title')
t2 = dt.get('타이틀')

print('title:', t1)
print('타이틀:', t2)  # None



