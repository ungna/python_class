# 리스트 삭제
# 리스트의 요소를 삭제
# del 리스트[인덱스]

#%%
a = [1,3,5]
print(a)

del a[1]

print(f'del a[1]: list:{a}, len:{len(a)}')

#%%

# 슬라이스(slice)를 사용하여 삭제
# 전체 삭제
del a[:]
print(f'전체삭제: list:{a}, len:{len(a)}')

#%%

# 데이터를 삭제: 자료 없음
a = [1,3,5]
print(a, id(a))

del a[:]
print(a, id(a))

#%%

a = [1,3,5]
b = a
print('a:', a, id(a))

# 새로운 메모리 할당
a = []
print('a:', a, id(a))
print('b:', b, id(b))

a = b
print('a:', a, id(a))
print('b:', b, id(b))

#%%
a = [1,3,5]
b = [1,3,5]
print('a:', a, id(a))
print('b:', b, id(b))

# 원래의 a의 리스트는 사라짐
a = b
print('a:', a, id(a))
print('b:', b, id(b))
