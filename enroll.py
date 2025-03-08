import sys
import tkinter as tk
from tkinter import ttk
import subprocess  # For opening coursesdata.py

# Fetch course name and price from command-line arguments
if len(sys.argv) > 2:
    selected_course = sys.argv[1]
    selected_price = sys.argv[2]
else:
    selected_course = "Unknown Course"
    selected_price = "₹ 0"

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
    print(f"Price: {price_entry.get()}")
    
    referral_code = referral_entry.get()
    if referral_code:
        print(f"Referral Code: {referral_code}")
    else:
        print("No Referral Code Entered (Optional)")

def open_courses():
    root.destroy()  # Close the signup form
    subprocess.Popen(["python", "corsesdata.py"])  # Open coursesdata.py

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

# State Dropdown with all 29 Indian states
states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
          "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
          "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
state_var = tk.StringVar()
state_label = tk.Label(root, text="Select State", font=("Arial", 10))
state_label.pack(anchor="w", padx=10, pady=(10, 0))
state_dropdown = ttk.Combobox(root, textvariable=state_var, values=states)
state_dropdown.pack(fill="x", padx=10, pady=5)

# Apply Code Button
apply_code_button = tk.Button(root, text="Apply Code", bg="yellow", command=submit_form)
apply_code_button.pack(pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", bg="green", fg="white", command=submit_form)
submit_button.pack(pady=10)

# Select Courses Button
select_courses_button = tk.Button(root, text="Select Courses", bg="blue", fg="white", command=open_courses)
select_courses_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
