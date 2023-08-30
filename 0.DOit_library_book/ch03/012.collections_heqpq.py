# 수상자 3명을 선정하려면?
# collections.heapq: 순위가 가장 높은 자료를 먼저 꺼내는 큐
# https://docs.python.org/ko/3/library/heapq.html

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

# 오름차순으로 지정됨
print(heapq.nsmallest(3, data))

#%%
# 내림차순도 가능
print(heapq.nlargest(3, data))

#%%
# len을 이용해 sort가능
print(heapq.nsmallest(len(data), data))

for x in range(len(data)):
    print(heapq.heappop(data))
    
#%%
# 정석대로 하려면은 heaq을 만들고 pop을 사용해 데이터를 꺼낸다
# 힙데이터를 생성하려면 heapq.heappush(), heapq.heapify()를 사용해야됨
# 위에서는 생성, pop과정을  nsmallest 한줄로 처리함

 # heapq에서 데이터의 우선순위를 비교하는 항목은 제일 앞에 있어야한다.
data = [
    (12.23, "강보람"),  # ("강보람", 12.23) 이렇게하면 "강보람"을 비교함
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


# heappush사용 

h = []  # 힙 생성

 # score은 (기록, 이름) 형식의 튜플
for score in data:   
    heapq.heappush(h, score) # heap에 데이터 저장

# 저장될때는 sort되는게 아니고 무작위로 저장되는거같음
# 근대 pop을 쓰면 최소값부터 반환됨
print(h)

# heappop을 사용해 최솟값부터 힙 반환
for i in range(3):
    print(heapq.heappop(h))
    

#%% 
# heapq.heapify()
# heapq.heapify()를 사용하면 push쓸때보다 많이 생략된다

heapq.heapify(data)  # data를 힙구조에 맞게 변경

# 바로 heappop 사용
for i in range(3):
    print(heapq.heappop(data))


