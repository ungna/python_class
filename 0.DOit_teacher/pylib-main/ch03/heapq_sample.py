
# 우선순위 큐

import heapq

data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]

# 오름차순으로 지정된 수만 참조
print(heapq.nsmallest(3, data))

#%%

l = len(data)
print(heapq.nsmallest(l, data))

# heapq 객체 생성
h = []
for score in data:
    heapq.heappush(h, score)

#%%
# 가장 작은 값에서 큰 순서로 꺼냄: 오름차순
lh = len(h)
for x in range(lh): 
    print(heapq.heappop(h)) # 꺼내고 삭제

print(h, type(h)) # []


