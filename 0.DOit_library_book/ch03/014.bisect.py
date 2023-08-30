# 점수에 따른 학점을 구하려면?
# bisect: 이진탐색 알고리즘을 구현한 모듈로 정렬된 리스트에 값을 삽입할 때 정렬을 유지할 수 있는 인덱스를 반환한다.
# https://docs.python.org/ko/3/library/bisect.html

import bisect

scores = [33, 99, 77, 70, 89, 90, 100]
grades = 'FDCBA'

# 기준점 이상
result = []
for score in scores:
    # 점수가 정렬되어 삽입될 수 있는 포지션을 반환 
    pos = bisect.bisect([60, 70, 80, 90], score)  
    grade = grades[pos]   # [0] 60 [1] 70 [2] 80 [3] 90 [4]  # 인덱스가 이렇게 들어감  
    result.append(grade)

print(scores)
print(result)

#%%
# bisect.bisect_left
# 기준점 초과
result =[]
for score1 in scores:
    pos = bisect.bisect_left([60, 70, 80, 90], score1)
    grade = grades[pos]
    result.append(grade)


