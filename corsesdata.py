import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

# Ensure UTF-8 encoding to prevent Unicode errors
sys.stdout.reconfigure(encoding='utf-8')

# Course data with INR instead of ₹
courses = [
    {"name": "Personal Branding", "image": "personal_branding.png", "price": "INR 635"},
    {"name": "Soft Skills Mastery", "image": "soft_skills.png", "price": "INR 1331"},
    {"name": "Digital Marketing Mastery", "image": "digital_marketing.png", "price": "INR 2499"},
    {"name": "Online Marketing Mastery", "image": "online_marketing.png", "price": "INR 4375"},
    {"name": "Finance Mastery", "image": "finance.png", "price": "INR 8750"},
    {"name": "Data Science", "image": "data_science.png", "price": "INR 12499"}
]

def open_course_details(course_name):
    course_mapping = {
        "Soft Skills Mastery": "softskills.py",
        "Digital Marketing Mastery": "digital.py",
        "Online Marketing Mastery": "online.py",
        "Finance Mastery": "finance.py",
        "Data Science": "datascience.py",
        "Personal Branding": "prsnl.py"
    }
    
    if course_name in course_mapping:
        subprocess.Popen(["python", course_mapping[course_name]])
    else:
        print("Course not found!")

def enroll_in_course(course_name, course_price):
    print(f"DEBUG: Opening enrollment for {course_name} at {course_price}")  # Debugging
    subprocess.Popen(["python", "enroll.py", course_name, course_price])

# Main window
root = tk.Tk()
root.title("Courses")
root.geometry("900x600")
root.configure(bg="white")

# Title Label
title_label = tk.Label(root, text="AA Bundle Courses", font=("Arial", 20, "bold"), bg="white")
title_label.pack(pady=10)

# Create course frames
frame = tk.Frame(root, bg="white")
frame.pack()

row, col = 0, 0
for course in courses:
    try:
        img = Image.open(course["image"])
        img = img.resize((250, 150), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading {course['image']}: {e}")
        img = None

    course_frame = tk.Frame(frame, bg="white", bd=2, relief="solid")
    course_frame.grid(row=row, column=col, padx=10, pady=10)

    if img:
        img_label = tk.Label(course_frame, image=img, bg="white")
        img_label.image = img  # Keep reference
        img_label.pack()

    name_label = tk.Label(course_frame, text=course["name"], font=("Arial", 12, "bold"), bg="white")
    name_label.pack()

    price_label = tk.Label(course_frame, text=course["price"], font=("Arial", 10), fg="green", bg="white")
    price_label.pack()

    btn_view = tk.Button(course_frame, text="View Course", bg="blue", fg="white", 
                         command=lambda c=course["name"]: open_course_details(c))
    btn_view.pack(pady=5)
    
    btn_buy = tk.Button(course_frame, text="Buy Now", bg="red", fg="white", 
                        command=lambda c=course["name"], p=course["price"]: enroll_in_course(c, p))
    btn_buy.pack(pady=5)

    col += 1
    if col > 2:
        col = 0
        row += 1

root.mainloop()
