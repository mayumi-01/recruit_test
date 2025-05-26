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

    with open("sql/delete1.sql") as f:
        sql_delete = f.read()

    with open("sql/insert1.sql") as f:
        sql_insert = f.read()

    try:
        cur.execute(sql_delete)
        cur.execute(sql_insert)
        conn.commit()
    except:
        conn.rollback()
        raise
