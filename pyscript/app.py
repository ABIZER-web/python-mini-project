import sqlite3
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

def create_database():
    conn = sqlite3.connect("AA1.db")
    cursor = conn.cursor()
    
    # Example table (Modify as needed)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        course_id INTEGER,
        enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    ''')
    
    conn.commit()
    conn.close()

@app.route("/")
def home():
    if 'user_id' in session:
        return f"Welcome, {session['user_name']}! <a href='/logout'>Logout</a>"
    return render_template("index.html")  # Serving index.html

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        
        conn = sqlite3.connect("AA1.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            conn.close()
            return redirect("/login")  # Redirect to login after successful registration
        except sqlite3.IntegrityError:
            return "Email already exists. <a href='/register'>Try again</a>"
    
    return render_template("register.html")  # Create a register.html file for registration form

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        conn = sqlite3.connect("AA1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            return redirect("/")
        else:
            return "Invalid email or password. <a href='/login'>Try again</a>"
    
    return render_template("login.html")  # Create a login.html file for login form

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect("/")

def main():
    create_database()
    print("Database 'AA1.db' and tables created successfully.")
    app.run(debug=True)

if __name__ == "__main__":
    main()
