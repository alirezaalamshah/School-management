import sqlite3

DB_PATH = "school.db"

def connect():
    return sqlite3.connect(DB_PATH)

def execute_query(query, params=()):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

def fetch_all(query, params=()):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
