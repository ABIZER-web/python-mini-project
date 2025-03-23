import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import bcrypt  
import os

# Function to verify password
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password)

# Function to fetch purchased courses
def get_purchased_courses(email):
    conn = sqlite3.connect("aa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM users WHERE email=?", (email,))
    courses = cursor.fetchall()
    conn.close()

    return [course[0] for course in courses] if courses else []

# Function to handle user login
def login():
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showwarning("Login", "Please enter both email and password.")
        return

    conn = sqlite3.connect("aa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE email=?", (email,))
    result = cursor.fetchone()

    if result and verify_password(password, result[0]):  
        messagebox.showinfo("Login", "Login Successful!")

        # Store login attempt
        cursor.execute("INSERT INTO login_attempts (email) VALUES (?)", (email,))
        conn.commit()

        # Fetch and display purchased courses
        courses = get_purchased_courses(email)
        if courses:
            courses_str = "\n".join(courses)
            messagebox.showinfo("Your Courses", f"You have purchased:\n{courses_str}")
        else:
            messagebox.showinfo("Your Courses", "No courses found!")
    else:
        messagebox.showwarning("Login", "Invalid Email or Password")

    conn.close()

# Function to handle password reset
def reset_password():
    email = email_entry.get()
    if not email:
        messagebox.showwarning("Reset Password", "Please enter your email to reset your password.")
        return
    messagebox.showinfo("Reset Password", "Reset password link has been sent to your email.")

# GUI Setup
root = tk.Tk()
root.title("Login to AA")
root.state("zoomed")  # Maximize the window

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Load and display the logo
logo_label = None  # Ensure global reference
image_path = "AA.jpg"
if os.path.exists(image_path):
    try:
        image = Image.open(image_path)
        image = image.resize((100, 100))  # Remove deprecated ANTIALIAS
        logo = ImageTk.PhotoImage(image)
        logo_label = tk.Label(frame, image=logo)
        logo_label.image = logo  # Keep a reference
        logo_label.grid(row=0, column=0, columnspan=2, pady=10)
    except Exception as e:
        print("Error loading image:", e)
else:
    print("Image file not found:", image_path)

email_label = tk.Label(frame, text="Email*")
email_label.grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = tk.Label(frame, text="Password*")
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

login_button = tk.Button(frame, text="Login", bg="green", fg="white", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=5)

reset_button = tk.Button(frame, text="Reset Password", bg="blue", fg="white", command=reset_password)
reset_button.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()