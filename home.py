import tkinter as tk
from tkinter import messagebox
import subprocess

def show_home():
    messagebox.showinfo("Home", "Welcome to the Home Page!")

def show_courses():
    messagebox.showinfo("Courses", "Here are the available courses.")

def show_about_us():
    messagebox.showinfo("About Us", "Learn more about us here.")

def show_contact_us():
    messagebox.showinfo("Contact Us", "Contact us at contact@example.com.")

def enroll():
    subprocess.Popen(["python", "enroll.py"])

def show_login():
    subprocess.Popen(["python", "login.py"])

# Create the main window
root = tk.Tk()
root.title("Home Page")

# Create and place the navigation buttons
home_button = tk.Button(root, text="Home", command=show_home)
home_button.grid(row=0, column=0, padx=10, pady=10)

courses_button = tk.Button(root, text="Courses", command=show_courses)
courses_button.grid(row=0, column=1, padx=10, pady=10)

about_us_button = tk.Button(root, text="About Us", command=show_about_us)
about_us_button.grid(row=0, column=2, padx=10, pady=10)

contact_us_button = tk.Button(root, text="Contact Us", command=show_contact_us)
contact_us_button.grid(row=0, column=3, padx=10, pady=10)

enroll_button = tk.Button(root, text="Enroll", command=enroll)
enroll_button.grid(row=0, column=4, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=show_login)
login_button.grid(row=0, column=5, padx=10, pady=10)

# Start the main event loop
root.mainloop()