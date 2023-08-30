# 데이터를 보기 좋게 출력하려면
# pprint: pretty print
# https://docs.python.org/ko/3/library/pprint.html

import pprint

# 딕셔너리, json format을 한눈에 알아보기 어려운 것을 보기 좋게 출력해준다

result = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

pprint.pprint(result)

#%% 
# import 해올때 as pp 로 하면은 import해온거 대신 쓸수있음
import pprint as pp

pp.pprint(result)
