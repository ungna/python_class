# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 10:22:50 2023

@author: Solero
"""
"""
[문제] 가진 돈으로 음료수 구매
조건: 가진 돈의 가장 비싼 음료수를 구매
생수   : 1000원
콜라   : 2000원
사이다 : 3000원
커피   : 4000원
"""

#%%

m = 5000

if m >= 1000:
    print("생수 구매")
elif m >= 2000:
    print("콜라 구매")
elif m >= 3000:
    print("사이다 구매")
elif m >= 4000:
    print("커피 구매")
else:
    print("구매하지 못함")

# 오답: 생수 구매
# 정답: 커피 구매

#%%

# if 조건을 큰 값부터 처리    
m = 3500

if m >= 4000:
    print("커피 구매")
elif m >= 3000:
    print("사이다 구매")
elif m >= 2000:
    print("콜라 구매")
elif m >= 1000:
    print("생수 구매")
else:
    print("구매하지 못함")
    
# 커피 구매

#%%

# if 조건을 작은 값부터 처리하라

m = 5500

if m < 1000:
    print("구매하지 못함")
elif m < 2000:    
    print("생수 구매")
elif m < 3000:    
    print("콜라 구매")
elif m < 4000:
    print("사이다 구매")
else:
    print("커피 구매")

#%%

# [문제] 위 문제에서 1000원 미만과 1000원 이상 처리하고
# 가진 돈으로 구매할 수있는 음료를 선택

m = 1999

if m >= 1000:
    print("음료수를 구매할 수 있습니다.")
    if m < 2000:    
        print("생수 구매")
    elif m < 3000:    
        print("콜라 구매")
    elif m < 4000:
        print("사이다 구매")
    else:
        print("커피 구매")
else:    
    print("음료수를 구매할 수 없습니다.")


