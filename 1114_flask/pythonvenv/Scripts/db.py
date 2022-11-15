import pymysql
import pymysql.cursors

# DB 연결하기

# 데이터베이스에 접근 함수 제작


def db_connection():
    db = pymysql.connect(
        host="localhost",
        port=3307,
        user="root",
        passwd="1234",
        db="aitrading_db",
        charset="utf8",
        cursor=db.cursor(pymysql.cursors.DictCursor)
    )
    # 커서 가져오기
    # cursor  데이터베이스와 상호 작용하는 데 사용하는 개체
    # dict으로 결과를 반환하겠다
    return db


def company():
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT * FROM `aitrading_db`.`companylist` LIMIT 100;'
    # SQL query 실행
    cur.execute(sql)
    # SQL query 실행 결과를 가져온다.
    result = cur.fetchall()
    db.close()
# excute()와 fetch()를 이용해 데이터 핸들링이 가능하다.
# excute() 를 이용해 SQL을 실행하고,
# 결과는 fetchall()을 이용해서 받아온다.
    return result
