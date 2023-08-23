# 리스트


#%%

# 리스트의 요소에 다른 리스트를 저장
e = [1,2,['Life', 'is']]
print(e)

#%%

# e[-1] 요소를 참조
ex = e[-1]
ex[0] = 99
print(ex, id(ex))
print(e)

# 새로운 리스트 메모리를 참조
print("새로운 리스트 메모리를 참조")
ex = [10,20,30]
print(ex, id(ex))

print("e와 ex는 관계가 끊김")
ex[-1] = 'ex'
print(ex, id(ex))

# e는 변화가 없다.
print('e:', e)




