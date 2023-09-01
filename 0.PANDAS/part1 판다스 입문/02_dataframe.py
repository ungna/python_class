# 판다스
# conda activate ENV   (내가만든 가상환경의 이름)
# pip install pandas

# 데이터프레임: DataFrame
# 2차원 배열, 행렬
# 여러개의 시리즈들이 한데 모여서 이룸 like 엑셀
# 딕셔너리 안에 values값을 리스트로 만들어서 데이터프레임으로 변환하는 방식을 주로씀

import pandas as pd

# dict
dict_data = {
    'c0' : [1, 2, 3],     # 칼럼, 시리즈 
    'c1' : [4, 5, 6],     # 칼럼, 시리즈 
    'c2' : [7, 8, 9],     # 칼럼, 시리즈 
    'c3' : [10, 11, 12],    # 칼럼, 시리즈 
    'c' : [13, 14, 15]     # 칼럼, 시리즈     
    }

# 데이터프레임으로 변경
fd = pd.DataFrame(dict_data)

print(type(fd))    # <class 'pandas.core.frame.DataFrame'>
print(fd)


# values 안에 list의 길이가 같아야됨
"""
dict_data = {
    'c0' : [1, 2, 3],    
    'c1' : [4, 5, 6],  
    'c2' : [7, 8, 9], 
    'c3' : [10, 11, 12],  
    'c' : [13, 14, 15, 16]  # 혼자 4개있으면은 에러
    }
# ValueError: All arrays must be of the same length
"""


#%%
# default 인덱스는 숫자, c숫자 형식으로 나옴
print(fd)

"""
   c0  c1  c2  c3   c
0   1   4   7  10  13
1   2   5   8  11  14
2   3   6   9  12  15
"""

