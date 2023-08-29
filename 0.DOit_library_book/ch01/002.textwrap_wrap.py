# textwrap.wrap은 문자열이 너무 길때 원하는 길이로 줄바꿈할 때 사용
# textwrap 공식문서: https://docs.python.org/ko/3/library/textwrap.html
import textwrap

long_text = "Life is too short, you need python. " * 10

#%%
# long_text를 단어가 잘리지 않게 70자 단위로 줄바꿈하기

# step1. 긴 문자열을 width길이만큼 자르고 이를 리스트로 만들어 반환한다
# 단어 단위로 문자열을 자르므로 단어 중간이 끊어지지는 않는다
result = textwrap.wrap(long_text, width = 70)


# step2. join을 사용해 리스트 형태의 result를 하나의 문자열로 표시한다
result2 = '\n'.join(result)
print(result2)
#%%

# variable explorer에서 list 형태로 나눠져 있는거 확인가능
print(f'첫번째 list: {result[0]}')
print(f'두번째 list: {result[1]}')

#%%
# textwrap.fill()
# 2단계로 나눠서 하지않고 textwrap.fill()을 사용해 한번에 처리할수있다

result3 = textwrap.fill(long_text, width = 70)
print(result3) 