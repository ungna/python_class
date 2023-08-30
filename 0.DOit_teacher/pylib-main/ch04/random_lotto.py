
# 
# 난수 
# [문제] 로또함수를 만들어라.
# 1. 당첨번호 : 난수 6개를 만들어라.
# 2. 임의의 숫자 6개를 콘솔창에서 입력을 받으라.
#     입력: 10,20,30,40,41,45
# 3. 당첨 유무를 확인하라. 

import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)  # 1~45 사이의 숫자중 임의의 숫자 생성
    result.append(num)

print(result)  # 무작위 생성된 6개의 숫자 출력

#%%
