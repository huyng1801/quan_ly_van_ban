import mysql.connector
from flask import Flask, g

app = Flask(__name__)

DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'quan_ly_van_ban',
}

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    return g.db

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.teardown_appcontext
def teardown_db(error):
    print(f"Lỗi khi thực hiện truy vấn: {str(error)}")
    close_db()

def execute_query(query, values=None, fetchone=False, fetchall=False, commit=False):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        if commit:
            db.commit()
        elif fetchone:
            result = cursor.fetchone()
            return result
        elif fetchall:
            results = cursor.fetchall()
            return results

    except Exception as e:
        print(f"Lỗi khi thực hiện truy vấn: {str(e)}")
        db.rollback()
    finally:
        cursor.close()