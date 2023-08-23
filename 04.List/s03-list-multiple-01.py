# 리스트 연산
# 리스트 곱하기(반복하기)
# 순서가 유지 된다.
# 리스트 = 리스트 * 정수

#%%
a = [1,3,5]
c = a * 3

print(c)

"""
# 결과: [1,3,5]을 3번 반복하여 합친다.
[1, 3, 5, 1, 3, 5, 1, 3, 5]
"""

#%%

# 리스트의 길이
l = len(c)
print('print:', l)

#%%

def multi(x, z):
    y = []
    for e in x:
        y.append(e * z)
    return y

print(multi([1,3,5], 3))
print(multi([1,2,3,4,5], 2))

    
