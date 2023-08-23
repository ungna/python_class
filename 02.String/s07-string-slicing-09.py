# 문자열 슬라이싱(Slicing)
# 문자열의 위치를 참조를 통해서 특정한 범위의 문자열을 추출
# 추출된 문자열은 새로운 변수를 할당하며 원본의 변화는 없다.
#############################################################
# 문자열[시작번호:끝번호]
# 시작위치: 0부터 시작
# 종료위치: 마지막값 - 1

s = "0123456789"
print(s)

# 끝의 내용 추출
print(s[-1:])   # 9
print(s[-2:])   # 89
print(s[-3:])   # 789
print(s[-4:])   # 6789

print(s[len(s) * -1 :]) # 처음부터 끝까지: 0123456789