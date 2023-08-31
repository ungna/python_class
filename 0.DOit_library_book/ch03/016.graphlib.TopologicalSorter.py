# 수강할 과목의 순서를 구하려면?
# graphlib.TopologicalSorter
# 선후관계가 정의된 그래프 구조에서 선후관계에 따라 정렬하고자 할때 사용
# https://docs.python.org/ko/3/library/graphlib.html

from graphlib import TopologicalSorter
# 선후관계의 가장 대표적인예: 대학 선수과목

# 영어 초급 -> 영어중급 -> 영어고급
#                -> 영어문법 -> 영어고급
#                         -> 영어회화


ts = TopologicalSorter()

# 규칙1
ts.add('영어중급', '영어초급')  # 중급 선수과목은 초급
ts.add('영어고급', '영어중급')  # 고급 선수과목은 중급

# 규칙2 
ts.add('영어문법', '영어중급')  # 문법 선수과목은 중급
ts.add('영어고급', '영어문법')  # 고급 선수과목은 문법

# 규칙3
ts.add('영어회화', '영어문법')

# 다음 순서대로 수강하면된다
print(list(ts.static_order()))

#%%
# 선행노드를 여러개 추가
ts.add('영어고급', '영어중급', '영어문법')  # 고급의 선수과목은 중급, 문법