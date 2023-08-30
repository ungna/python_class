
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

#%%

# [주의] heappush()를 사용하지 않은 리스트를 heappop()을 사용하지 말라.
# 힙 데이터를 생성 : heapq.heapify(), heapq.heappush()를 해서 사용

l = len(data)

# 힙 데이터 생성
heapq.heapify(data)

for x in range(l):
    print(heapq.heappop(data))

