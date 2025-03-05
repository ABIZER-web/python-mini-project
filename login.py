import tkinter as tk
from tkinter import messagebox

def login():
    email = email_entry.get()
    password = password_entry.get()
    # Here you can add your login logic
    if email and password:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showwarning("Login", "Please enter both email and password.")

def reset_password():
    # Here you can add your reset password logic
    messagebox.showinfo("Reset Password", "Reset password link has been sent to your email.")

# Create the main window
root = tk.Tk()
root.title("Login to Millionaire Track")

# Create and place the email label and entry
email_label = tk.Label(root, text="Email*")
email_label.grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the password label and entry
password_label = tk.Label(root, text="Password*")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place the reset password button
reset_button = tk.Button(root, text="Reset Password", command=reset_password)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()