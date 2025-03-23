import sqlite3
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess  # For opening coursesdata.py
import bcrypt  # Secure password hashing

# Fetch course name and price from command-line arguments
if len(sys.argv) > 2:
    selected_course = sys.argv[1]
    selected_price = sys.argv[2]
else:
    selected_course = "Unknown Course"
    selected_price = "₹ 0"

# Database Setup
def setup_database():
    conn = sqlite3.connect("aa.db")
    cursor = conn.cursor()
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
    conn.commit()
    conn.close()

setup_database()  # Ensure database is created

# Function to hash passwords
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

# Function to handle form submission
def submit_form():
    if email_entry.get() != confirm_email_entry.get():
        messagebox.showerror("Error", "Emails do not match!")
        return
    
    if not state_var.get():
        messagebox.showerror("Error", "Please select a state!")
        return
    
    hashed_password = hash_password(password_entry.get())  # Hash password securely
    
    conn = sqlite3.connect("aa.db")  
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, username, email, dob, state, mobile, password, referral_code, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (name_entry.get(), username_entry.get(), email_entry.get(), dob_entry.get(), state_var.get(), mobile_entry.get(), hashed_password, referral_entry.get(), price_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username, Email, or Mobile already exists!")
    finally:
        conn.close()

# Function to open courses page
def open_courses():
    root.destroy()
    subprocess.Popen(["python", "corsesdata.py"])

# Creating main window
root = tk.Tk()
root.title(f"Enroll in {selected_course}")
root.geometry("400x600")

# Title Label
title_label = tk.Label(root, text=f"Enroll in {selected_course}", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Labels and Entries
fields = ["Name As Per Aadhaar Card", "Username", "Email", "Confirm Email", "Date of Birth", "Mobile No.", "Password", "Referral Code", "Price"]
entries = []

for i, field in enumerate(fields):
    label = tk.Label(root, text=field, font=("Arial", 10))
    label.pack(anchor="w", padx=10, pady=(10, 0))
    entry = tk.Entry(root, show="*" if "Password" in field else "")
    entry.pack(fill="x", padx=10, pady=5)
    entries.append(entry)

name_entry, username_entry, email_entry, confirm_email_entry, dob_entry, mobile_entry, password_entry, referral_entry, price_entry = entries

# Pre-fill the price field
price_entry.insert(0, selected_price)

# State Dropdown
states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
state_var = tk.StringVar()
state_label = tk.Label(root, text="Select State", font=("Arial", 10))
state_label.pack(anchor="w", padx=10, pady=(10, 0))
state_dropdown = ttk.Combobox(root, textvariable=state_var, values=states)
state_dropdown.pack(fill="x", padx=10, pady=5)

# Buttons
submit_button = tk.Button(root, text="Submit", bg="green", fg="white", command=submit_form)
submit_button.pack(pady=10)

select_courses_button = tk.Button(root, text="Select Courses", bg="blue", fg="white", command=open_courses)
select_courses_button.pack(pady=10)

# Run Tkinter event loop
root.mainloop()