# 리스트 함수 : index(값)

#%%
a = list("ABCDEFGHIJKL")
print(a)

#%%

v = 'G'
x = a.index(v)
print(f"리스트 {a}에서 ('{v}')값이 있는 인덱스 위치는 ({x}) 번째이다.")

#%%

# 찾는 값이 없으면 예외 발생
# ValueError: 'Z' is not in list
print(a.index('Z'))
