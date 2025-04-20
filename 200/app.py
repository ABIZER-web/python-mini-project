from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'attendance.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    ''')

    # Students table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        name TEXT
    )
    ''')

    # Attendance table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        student_id TEXT,
        subject TEXT,
        date TEXT,
        status TEXT
    )
    ''')

    # Insert students
    students = [
        ('23IT1018', 'HARSIMRAN KAUR GURM'),
        ('23IT1029', 'HUSAIN LALJI'),
        ('23IT1041', 'KANDE ANIKET PANDHARI'),
        ('23IT1020', 'NAIR SHREYAS SUNIL')
    ]
    cursor.executemany('INSERT OR IGNORE INTO students VALUES (?, ?)', students)

    # Insert users
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('teacher1', 'pass123', 'teacher')")
    for student_id, _ in students:
        cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, 'pass123', 'student')", (student_id,))

    conn.commit()
    conn.close()

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ? AND role = ?', 
                        (username, password, role)).fetchone()
    conn.close()

    if user:
        if role == 'student':
            return redirect(url_for('student_dashboard', student_id=username))
        elif role == 'teacher':
            return redirect(url_for('teacher_dashboard'))
    else:
        return "Invalid credentials", 401

@app.route('/student-dashboard')
def student_dashboard():
    student_id = request.args.get('student_id')

    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE student_id = ?', (student_id,)).fetchone()
    conn.close()

    if student:
        return render_template('student-dashboard.html', student_id=student['student_id'], student_name=student['name'])
    else:
        return "Student not found", 404

@app.route('/view-students')
def view_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('view-students.html', students=students)

@app.route('/manage-attendance')
def manage_attendance():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('manage-attendance.html', students=students)

@app.route('/teacher-dashboard')
def teacher_dashboard():
    return render_template('teacher-dashboard.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
