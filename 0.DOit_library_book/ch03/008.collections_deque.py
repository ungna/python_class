# 앞뒤에서 자료를 넣고 빼려면?
# collections.deque: 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형이다
# 스택(stack)처럼 써도 큐(queue)처럼 써도된다
# https://docs.python.org/ko/3/library/collections.html#collections.deque

# 큐: 한쪽은 추가만 반대쪽은 삭제만 가능한 구조 (선입선출)
# 스택: 한쪽 끝으로만 추가 삭제가 가능한 구조 (후입선출)


from collections import deque

# 시계 반시계 방향으로 돌리기

a = [1, 2, 3, 4, 5]
print(id(a))

q = deque(a)   # 데크로 할때 id가 바뀜
# 시계방향(오른쪽)은 양수  반시계(왼쪽)는 음수
q.rotate(2)   # rotate 등 사용해도 id는 그대로

print(q, id(q))    # deque([4, 5, 1, 2, 3])

# 다시 리스트 형식으로
r = list(q)
print(r, id(r))   # [4, 5, 1, 2, 3]

# 참조만 하기때문에 데이터는 사라지지 않는다
print(a)       # [1, 2, 3, 4, 5]
# %%

# append,  appendleft

a = [1, 2, 3, 4]
d = deque(a)

d.append(5)  # [1,2,3,4,5]
d.appendleft(0)  # [0,1,2,3,4,5]


# %%
# pop,  popleft
# pop을 쓰면 리스트에서 값을 끄집어 냄  즉 원래있던 리스트에서 사라짐

a = [0, 1, 2, 3, 4, 5]
r = deque(a)

p = r.pop()    # p = 5
q = r.popleft()  # q = 0

print(r)      # deque([1, 2, 3, 4])

# %%
# pop
# pop을 쓰면 리스트에서 값을 끄집어 냄  즉 원래있던 리스트에서 사라짐

a = [0, 1, 2]
r = deque(a)

p = r.pop()  # 2
p = r.pop()  # 1
p = r.pop()  # 0
# p = r.pop()  # IndexError: pop from an empty deque

print(r)  # deque([])

#%%
# 중간에 있는거 pop 쓰기

# a에서 2 제거하기
a = [0, 1, 2, 3, 4, 5]

# 지정된 인덱스 요소를 꺼냄
print(a[2])
a.pop(2)
print(a)

# %%
# 중간에 있는거 pop 쓰기
# rotate랑 연계

# a에서 2 제거하기
a = [0, 1, 2, 3, 4, 5]

# 2를 젤 왼쪽에 넣기
r = deque(a)
r.rotate(-2)
print(r)

# popleft로 제거
r.popleft()
print(r)

# 다시 돌리기
r.rotate(2)

# list로 바꾸기
a = list(r)
print(a)

#%%
# 반복문을 사용해 계속 꺼내기  # 안됨
a = [1, 2, 5, 7]

while True:
    r = a.pop()  # IndexError: list index out of range
    print(r)
    # pop으로 다 빠져나와서 a[]으로 빈 리스트가 되면 break
    if a == []:
        break

# %%
# 반복문 while을 사용해 계속 꺼내기
a = [1, 2, 5, 7]

# a에 값이 존재하는 동안
while a:
    r = a.pop()
    print(r)  # 꺼낸거 확인
    print(a)  # 남아있는거 확인

# %%
# 반복문 for을 사용해 계속 꺼내기
a = [1, 2, 5, 7]

# i = range(0, len(a))번 반복
for i in range(0, len(a)):
    r = a.pop()
    print(r)