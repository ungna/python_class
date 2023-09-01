# 블로그 데이터를 저장하려면?
# sqlite3: SQLite 데이터베이스를 사용하는데 필요한 인터페이스 모듈
# https://docs.python.org/ko/3/library/sqlite3.html

# 인터넷에 sqlitebrowser 검색후 standard installer 다운

import sqlite3

# 접속
conn = sqlite3.connect("blog.db")

# 커서생성
cur = conn.cursor()

#%%

# 테이블 생성 한번만 실행
cur.execute("SELECT count(*) FROM sqlite_master WHERE name = 'blog'")
exist = cur.fetchone()
if exist[0] != 1:
    cur.execute("""
            CREATE TABLE blog(
                id integer PRIMARY KEY,
                subject text,
                content text,
                date text
                )
            """)
           

#%% 
# 데이터 입력

insert_sql = "INSERT INTO blog VALUES(%d, '%s', '%s', '%s')"
data = [
    (1, '첫번쨰 블로그', '첫번째 블로그 내용', '20230831'),
    (2, '두번쨰 블로그', '두번째 블로그 내용', '20230831'),
    (3, '세번쨰 블로그', '세번째 블로그 내용', '20230831')
]
try:
    for d in data:
        sql = insert_sql % (d[0], d[1], d[2], d[3])
        print(sql)
        cur.execute(sql)
        
except:
    print("sql실행오류")
    
finally:
    conn.commit()  # 서버에 데이터 저장
    conn.close()


#%%


insert_sql = "INSERT INTO blog VALUES(%d, '%s', '%s', '%s')"
data = [
    (4, '네번쨰 블로그', '네번째 블로그 내용', '20230831'),
    (5, '다섯번쨰 블로그', '네번째 블로그 내용', '20230831'),
    (6, '여섯번쨰 블로그', '네번째 블로그 내용', '20230831')
]
try:
    for d in data:
        sql = insert_sql % (d[0], d[1], d[2], d[3])
        print(sql)
        cur.execute(sql)
        
except:
    print("sql실행오류")
    
finally:
    conn.commit()
    conn.close()
