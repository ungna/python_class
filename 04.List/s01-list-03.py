# 리스트

# 리스트의 요소에 다른 리스트를 저장
e = [1,2,['Life', 'is']]
print(e)

#%%
print(e[0])
print(e[1])
print(e[2])  # ['Life', 'is']
print(e[-1]) # ['Life', 'is']

#%%
print(e[2][0]) # 'Life'
print(e[2][1]) # 'is'

#%%

print(e[-1][0]) # 'Life'
print(e[-1][1]) # 'is'

#%%

ex = e[-1]
print(ex[0]) # 'Life'
print(ex[1]) # 'is'



