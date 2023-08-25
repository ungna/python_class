# 문제1
a = "Life is too short, you need python"

if "wife" in a :
    print ("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a :
    print("shirt")           # 이게 나옴
elif "need" in a:
    print("need")
else:
    print("none")


#%%
# 문제2
# 3의 배수의 합
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
    
print(result)

#%% 별찍기
# 문제3
# 별찍기

i = 0
while True:
    i += 1
    if i > 5:
        break
    print("*"*i)

#%%
# 문제4
# for을 이용해 1~100 출력

for i in range(1,101):
    print(i)

#%%
# 문제5
# 반 평균 구하기
class_A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0

for score in class_A:
    total += score
    
average = total / len(class_A)

print(average)

#%%
# 문제6
# 홀수만 골라 2를 곱해 result에 넣어라
number = [1,2,3,4,5]
result = []
for n in number:
    if n % 2 == 1:             # if 조건에 맞는 n을 찾기 
        result.append(n*2)     # 찾은 n에 2를 곱해 result에 넣어라
print(result)

# 위 문장을 리스트 컴프리헨션을 이용해 작성하라        
number = [1,2,3,4,5]

# result = 표현식 for 변수 in 변수  if 조건문
result = [n * 2 for n in number if n % 2 == 1]

print(result)




