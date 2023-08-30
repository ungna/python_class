# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:52:40 2023

@author: Solero
"""

# 데이터를 보기 좋게 출력
# https://wikidocs.net/105471

# pprint : pretty print
# dict, json format을 보기 좋게 출력

import pprint as pp

# dict
result = { 'userId': 1, 'id': 1, 
          'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 
          'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

print(result)
print('-' * 50)

#%%

#pprint.pprint(result)
pp.pprint(result)



