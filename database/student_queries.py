# database/student_queries.py
from database.db import execute_query
from database.db import execute_query, fetch_all

def create_student_table():
    query = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        family TEXT NOT NULL,
        national_id TEXT UNIQUE NOT NULL,
        student_code TEXT UNIQUE NOT NULL,
        class_name TEXT NOT NULL,
        major TEXT NOT NULL
    )
    '''
    execute_query(query)

def add_student(name, family, national_id, student_code, class_name, major):
    query = '''
    INSERT INTO students (name, family, national_id, student_code, class_name, major)
    VALUES (?, ?, ?, ?, ?, ?)
    '''
    execute_query(query, (name, family, national_id, student_code, class_name, major))

def get_all_students():
    query = 'SELECT * FROM students'
    return fetch_all(query)

def delete_student(student_id):
    query = 'DELETE FROM students WHERE id = ?'
    execute_query(query, (student_id,))
