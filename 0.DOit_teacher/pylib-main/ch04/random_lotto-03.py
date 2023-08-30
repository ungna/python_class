
# 
# 난수 
# [문제] 로또함수를 만들어라.
# 1. 당첨번호 : 난수 6개를 만들어라.
# 2. 임의의 숫자 6개를 콘솔창에서 입력을 받으라.
#     입력: 10,20,30,40,41,45
# 3. 당첨 유무를 확인하라. 

import random

# 로또 번호 생성 함수
# start : 발행시작번호
# end : 발행종료번호
# num : 발행해야 할 번호의 갯수
def lottos(start, end, num):
    nums = [] # 생성된 번호를 담을 리스트
    while True:
        if len(nums) >= num: # 6개 번호 생성
            break
        nr = random.randint(start, end)  
        if nr not in nums: # 중복 체크
            nums.append(nr)
    return nums


#%%

# 당첨번호 확인
# nums : 입력번호
# lotto : 당첨번호
def lucky(nums, lotto):
    result = [0 for x in nums]
    nlen = len(nums)
    for n in range(nlen):
        if nums[n] in lotto:
            result[n] = 1
    return result

#%%

# 당첨번호 발행
lotto = lottos(1,45,6) 

# 당첨번호를 넣어서 검산
# 당첨번호를 섞어서 검산
# nums = [n for n in lotto]
# random.shuffle(nums)

# 로또번호 입력 : 1,2,3,4,5,6
"""
ms = ml.split(',')

nums = []
for m in ms:
    n = int(m) # 숫자로 변환
    nums.append(n)
"""
import sys
ml = input("로또 번호를 6개를 입력하세요: ")
nums = list(map(lambda x : int(x), ml.split(',')))
if len(nums) != 6:
    print(f"입력한 숫자의 갯수({len(nums)})가 잘못되었습니다.")
    sys.exit()

print("입력번호:", nums)    

#%%
prize = lucky(nums, lotto)
print("당첨번호:", lotto)
print("입력번호:", nums)
print("당첨유무:", prize)
print("당첨확인:", "당첨을 축하합니다" if all(prize) else "다음 기회에...")