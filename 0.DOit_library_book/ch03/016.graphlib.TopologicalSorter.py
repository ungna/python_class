# 수강할 과목의 순서를 구하려면?
# graphlib.TopologicalSorter
# 선후관계가 정의된 그래프 구조에서 선후관계에 따라 정렬하고자 할때 사용
# https://docs.python.org/ko/3/library/graphlib.html

from graphlib import TopologicalSorter
# 선후관계의 가장 대표적인예: 대학 선수과목

# 영어 초급 -> 영어중급 -> 영어고급
#                -> 영어문법 -> 영어고급
#                         -> 영어회화

