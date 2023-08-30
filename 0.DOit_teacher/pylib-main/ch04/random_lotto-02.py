
# 
# 난수 
# [문제] 로또함수를 만들어라.
# 1. 당첨번호 : 난수 6개를 만들어라.
# 2. 임의의 숫자 6개를 콘솔창에서 입력을 받으라.
#     입력: 10,20,30,40,41,45
# 3. 당첨 유무를 확인하라. 

import random

# 로또 번호 생성 함수
def lottos():
    nums = [] # 생성된 번호를 담을 리스트
    while True:
        if len(nums) >= 6: # 6개 번호 생성
            break
        num = random.randint(1, 45)  # 1~45 사이의 숫자중 임의의 숫자 생성
        if num not in nums: # 중복 체크
            nums.append(num)
    return nums


#%%

# 당첨번호 확인
def lucky(nums):
    result = [0,0,0,0,0,0]
    for n in range(6):
        if nums[n] in lotto:
            result[n] = 1
    return result

#%%

# 당첨번호 발행
lotto = lottos() 

# 로또번호 입력 : 1,2,3,4,5,6
ml = input("로또 번호를 6개를 입력하세요: ")
ms = ml.split(',')

nums = []
for m in ms:
    n = int(m) # 숫자로 변환
    nums.append(n)

print(nums)    

#%%
prize = lucky(nums)
print("당첨번호:", lotto)
print("입력번호:", nums)
print("당첨유무:", prize)
print("당첨확인:", "당첨을 축하합니다" if all(prize) else "다음 기회에...")