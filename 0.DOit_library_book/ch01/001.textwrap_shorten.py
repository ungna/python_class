# textwrap.shorten()은 문자열을 원하는 길이에 맞게 줄여 표시할때 사용
# textwrap 공식문서: https://docs.python.org/ko/3/library/textwrap.html
import textwrap

# 뒤에 [...]을 포함해서 길이15로 글자를 짜름
textwrap.shorten("Life is too short, you need python", width = 15)

#%%
# 한글도 길이 1로 처리
textwrap.shorten("인생은 짧으니 파이썬이 필요해", width = 15)
#%%

# 단어하나가 너무 길면 짤라짐
textwrap.shorten("01234567890123456789", width = 15)
textwrap.shorten("01234567890123456789", width = 50)

# 단어하나 기준은 띄어쓰기
textwrap.shorten("0 1 2 3 4 5 6 7 8 9", width = 15)

#%%
# 뒤에 생략되는 부분은 placeholder을 사용해 [...] 대신 원하는걸로 대체할 수 있다
# [...]은 포함안하고 길이 15로
textwrap.shorten("인생은 짧으니 파이썬이 필요해", width = 15, placeholder='...')