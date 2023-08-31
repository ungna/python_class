# 블로그 데이터를 저장하려면?
# sqlite3: SQLite 데이터베이스를 사용하는데 필요한 인터페이스 모듈
# https://docs.python.org/ko/3/library/sqlite3.html

# 쿼리로 만든 테이블 

import sqlite3

# 접속
conn = sqlite3.connect("blog.db")
# 커서생성
cur = conn.cursor()

# 쿼리입력
cur.execute("SELECT * FROM blog WHERE id IN(1,3,5,7,9)")
# 쿼리의 결과를 얻음: list 객체에 담음
data = cur.fetchall()  # 달라진 데이터 최신화하고 저장

for d in data:
    print(d)
    
conn.close()

#%%
import sqlite3

conn = sqlite3.connect("blog.db")
curr = conn.cursor()

def selectALL():
    cur.execute("SELECT * FROM blog")
    data = cur.fetchall()
    for d in data:
        print(d)
    
def delete(cur, id):
    sql =  "DELETE FROM blog WHERE id = ?"
    cur.execute(sql, (id))
    
def update(cur, _id, subject, content, date):
    sql = """
        UPDATE blog SET = ?, 
        content = ?, 
        date = ?, 
        WHERE id = ?
    """
    cur.execute(sql, (subject, content, date, id))

def insert(cur, id, subject, content, date):
    sql = "INSERT INTO blog VALUSE (?,?,?,?)"
    cur.execute(sql, (id, subject, content, date))    

#%%
# insert(curr, 999, "구구", "비둘기는 평화의 상징", "20230831")
selectALL(curr)
update(curr, 99, "구구단", "구구단을 외우자", "20230831")
selectALL(curr)
delete(curr, 99)
selectALL(curr)

#%%
conn.close()