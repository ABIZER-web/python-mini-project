import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Form Submitted!")
    print(f"Name: {name_entry.get()}")
    print(f"Username: {username_entry.get()}")
    print(f"Email: {email_entry.get()}")
    print(f"Confirm Email: {confirm_email_entry.get()}")
    print(f"State: {state_var.get()}")
    print(f"Date of Birth: {dob_entry.get()}")
    print(f"Mobile No: {mobile_entry.get()}")
    print(f"Password: {'*' * len(password_entry.get())}")
    print(f"Referral Code: {referral_entry.get()}")

# Creating main window
root = tk.Tk()
root.title("Signup Form")
root.geometry("400x500")

# Labels and Entries
fields = ["Name As Per Aadhaar Card", "Username", "Email", "Confirm Email", "Date of Birth", "Mobile No.", "Password", "Referral Code"]
entries = []

for i, field in enumerate(fields):
    label = tk.Label(root, text=field, font=("Arial", 10))
    label.pack(anchor="w", padx=10, pady=(10, 0))
    entry = tk.Entry(root, show="*" if "Password" in field else "")
    entry.pack(fill="x", padx=10, pady=5)
    entries.append(entry)

name_entry, username_entry, email_entry, confirm_email_entry, dob_entry, mobile_entry, password_entry, referral_entry = entries

# State Dropdown
state_var = tk.StringVar()
state_label = tk.Label(root, text="Select State", font=("Arial", 10))
state_label.pack(anchor="w", padx=10, pady=(10, 0))
state_dropdown = ttk.Combobox(root, textvariable=state_var, values=["Maharashtra", "Gujarat", "Delhi", "Karnataka", "Tamil Nadu"])
state_dropdown.pack(fill="x", padx=10, pady=5)

# Apply Code Button
apply_code_button = tk.Button(root, text="Apply Code", bg="yellow", command=submit_form)
apply_code_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
