

import bisect

# 학점: A,B,C,D,F

scores = [60, 33, 99, 77, 70, 89, 90, 99]
grades = 'FDCBA'

result = []
for score in scores: # 기준점수 이상
    # 점수가 정렬되어 삽입될 수 있는 포지션을 반환
    pos = bisect.bisect([60, 70, 80, 90], score)  
    grade = grades[pos]
    result.append(grade)

#%%

xscores = list(zip(scores, result))
print(xscores)

    