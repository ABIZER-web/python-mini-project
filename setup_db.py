import sqlite3

# Connect to SQLite database (creates one if it doesn't exist)
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create Users Table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    dob TEXT NOT NULL,
    state TEXT NOT NULL,
    mobile TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    referral_code TEXT,
    price TEXT NOT NULL
)''')

# Create Login Attempts Table
cursor.execute('''CREATE TABLE IF NOT EXISTS login_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

conn.commit()
conn.close()
print("Database and tables created successfully!")
