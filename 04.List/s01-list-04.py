# 리스트


#%%

# 리스트의 요소에 다른 리스트를 저장
e = [1,2,['Life', 'is']]
print(e)

#%%

ex = e[-1]
print(ex[0]) # 'Life'
print(ex[1]) # 'is'

#%%

# 리스트 e의 마지막 요소를 새로운 변수로 참조한 후
# 변경하면?

ex[0] = 'Go'
ex[1] = 'On'

print(ex, id(ex))
print(e, id(e))

#%%

# 리스트안의 리스트의 요소를 새로운 내용으로 변경하면
# 기존 그 요소를 가리키고 있는 변수는?
e[-1] = [10,20,30]
print(e, id(e))
print(e[-1], id(e[-1]))

# 새로 바뀌기 전의 내용을 가지고 있다.
print(ex, id(ex))
ex[0] = 99

print(ex, id(ex))





