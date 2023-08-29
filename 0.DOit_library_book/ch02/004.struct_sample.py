# c언어로 만든 데이터를 파이썬으로 읽어 내용확인
# struct 공식문서: https://docs.python.org/ko/3.9/library/struct.html
# 

import struct

print("# c to python struct")

with open("output.bin", 'rb') as f:
    chunk = f.read(16)
    up16 = 'di' + ('c'*4)
    result = struct.unpack(up16, chunk)
    print(result)
    
# 결과
# (7.5, 15, b'A', b'\xcc', b'\xcc', b'\xcc')


#%%
import struct

print("# c to python struct2")

with open("output2.bin", 'rb') as f:
    chunk = f.read(24)
    up24 = 'di' + ('c' * 12)
    result = struct.unpack(up24, chunk)
    print(result)   #  (7.5, 15, b'H', b'e', b'l', b'l', b'o', b'\x00', b'\xcc', b'\xcc', b'\xcc', b'\xcc', b'\xcc', b'\xcc')


# 받아온거를 리스트로 넣음 
# 이떄 왠지모르겠지만 표기가 10진수로 바뀜
lst = []
for x in range(2, len(result)):  # HELLO를 가지고 올거라 앞에 [0] :7.5 [1] :15 빼고 2부터
    lst += result[x]
    
print(lst)  # [72, 101, 108, 108, 111, 0, 204, 204, 204, 204, 204, 204]

# 리스트 형식을 문자열로 합치기
s = ''
for n in lst:
    if n == 0:
        break;
    s += chr(n)
    
print(s)  # Hello
