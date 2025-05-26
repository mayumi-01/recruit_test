import mysql.connector


if __name__ == "__main__":
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='mysql',
        database='testdb'
    )
    cur = conn.cursor()

    with open("sql/select.sql") as f:
        sql_select = f.read()

    with open("sql/insert2.sql") as f:
        sql_insert = f.read()

    cur.execute(sql_select)
    result = cur.fetchall()
    if len(result) == 0:
        try:
            cur.execute(sql_insert)
            conn.commit()
        except:
            conn.rollback()
            raise
