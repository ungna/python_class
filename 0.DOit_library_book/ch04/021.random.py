# random: 난수생성
# https://docs.python.org/ko/3/library/random.html

import random

result = []
while len(result) < 6:   # 뽑을개수 6개 설정
    num = random.randint(1, 45)  # 1~45까지 임의의 숫자 생성
    result.append(num)
    
print(result)

#%%
# 중복되는게 안오게 
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
        
print(result)

#%%
# shuffle choice
# shuffle: 리스트 요소를 무작위로 섞음
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)

# choice: 리스트 요소에서 무작위로 하나 선택
c_lst = random.choice(lst)
print(c_lst)

#%% 

# [문제]
# 난수 6개를 만들어라
# 임의의 숫자 6개를 콘솔창에서 입력받아라
# 당첨유무를 확인하라

import random

i = 0
my_num = []
result = []


# 로또번호
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

    
# print(result)

# 내번호 while
# 중복되거나 잘못입력하면 다시쓰게
# continue대신 break쓰면 바로 탈락시킬수있음
while i < 6:
    a = int(input(f'{i+1}번째: 1 ~ 45 사이의 값을 입력하세요:'))
    if a > 45 or a <= 0:   # 1~45까지 숫자만 입력되게
        print("잘못된 번호 입력 다시입력")
        continue
    elif a in my_num:   # 중복번호 안되게
        print("중복된 번호 입력 다시입력")
        continue
    else:
        my_num.append(a)
    i += 1    # continue하면 +1 안되게 젤 밑으로
  


# 당첨확인 sorted사용
result = sorted(result)
my_num = sorted(my_num)

if my_num == result:
    print(f"당첨!! {my_num}")
else:
    print(f"꽝입니다! 당첨번호:{result},  내번호: {my_num}")

#%%
# 입력 다르게 하기
# 내번호
# while 말고 for쓰고
# 중복 잘못입력하면 탈락
i = 0
my_num = []
result = []


# 로또번호
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
    
print(result)
#%%
# 내번호 for사용
#############################################
###### 바로탈락만되고 continue가 안됨  ######
#############################################
for i in range(1,7):
    a = int(input(f'{i}번째: 1 ~ 45 사이의 값을 입력하세요:'))
    if a > 45 or a <= 0:  # 1~45
        print("잘못된 번호 입력 자동탈락")
        continue
    elif a in my_num: # 중복이 안되게
        print("중복된 번호 입력 자동탈락")
        continue
    my_num.append(a)
print(my_num)

#%%
# 당첨확인 sorted 없이
result = [11, 39, 8, 30, 1, 2]
my_num = [39, 11, 8, 30, 2, 10]
for i in range(1,len(result)):
    # 길이가 같은지 6개 뽑아야되는데 그 이상이나 이하면은 바로 탈락
    if len(result) == len(my_num):
        pass
    else:
        print("개수안됨")
        break
    
    # 로또번호가 같은지 
    if my_num[i] in result:    
        print("참임", my_num[i])
    else: 
        print("거짓임", my_num[i])
    


#%%
# 입력 다르게 하기 -  로또 비교 생략

# 내번호
# map으로 한번에 여러개 입력
a, b, c, d, e, f = map(int, input('1 ~ 45 사이의 값을 6개 입력하세요:').split())
my_num = [a, b, c, d, e, f]
my_num = sorted(my_num)


