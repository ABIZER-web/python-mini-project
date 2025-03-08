import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

# Course data
courses = [
    {"name": "Personal Branding", "image": "personal_branding.png", "price": "\u20b9 635"},
    {"name": "Soft Skills Mastery", "image": "soft_skills.png", "price": "\u20b9 1331"},
    {"name": "Digital Marketing Mastery", "image": "digital_marketing.png", "price": "\u20b9 2499"},
    {"name": "Online Marketing Mastery", "image": "online_marketing.png", "price": "\u20b9 4375"},
    {"name": "Finance Mastery", "image": "finance.png", "price": "\u20b9 8750"},
    {"name": "Data Science", "image": "data_science.png", "price": "\u20b9 12499"}
]

def open_course_details(course_name):
    topics = {
        "Personal Branding": ["1. Canva", "2. Adobe Premiere Pro", "3. Adobe Photoshop"],
        "Soft Skills Mastery": ["1. Communication Skills", "2. Email Marketing"],
        "Digital Marketing Mastery": ["1. Google Ads", "2. Facebook Ads", "3. Microsoft Ads", "4. Power BI", "5. Machine Learning", "6. Python"],
        "Online Marketing Mastery": ["1. Instagram Marketing", "2. Instagram Reels Mastery", "3. LinkedIn Marketing", "4. YouTube Marketing", "5. Email Marketing"],
        "Finance Mastery": ["1. Option Trading", "2. Stock Market"],
        "Data Science": [
            "1. Canva", "2. Adobe Premiere Pro", "3. Adobe Photoshop",
            "4. Communication Skills", "5. Email Marketing", "6. Google Ads", "7. Facebook Ads", "8. Microsoft Ads",
            "9. Power BI", "10. Machine Learning", "11. Python", "12. Instagram Marketing", "13. Instagram Reels Mastery",
            "14. LinkedIn Marketing", "15. YouTube Marketing", "16. Email Marketing", "17. Option Trading", "18. Stock Market"
        ]
    }
    
    details_window = tk.Toplevel(root)
    details_window.title(f"{course_name} Course")
    details_window.geometry("500x600")
    details_window.configure(bg="white")

    tk.Label(details_window, text=f"{course_name} Course", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
    
    for topic in topics.get(course_name, []):
        tk.Label(details_window, text=topic, font=("Arial", 12), bg="white").pack(anchor="w", padx=20, pady=3)

# Main window
root = tk.Tk()
root.title("Courses")
root.geometry("900x600")
root.configure(bg="white")

# Title Label
title_label = tk.Label(root, text="Mt Bundle Courses", font=("Arial", 20, "bold"), bg="white")
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
    
    # Updated Buy Now Button
    btn_buy = tk.Button(course_frame, text="Buy Now", bg="red", fg="white", 
                        command=lambda c=course["name"], p=course["price"]: subprocess.Popen(["python", "enroll.py", c, p]))
    btn_buy.pack(pady=5)

    col += 1
    if col > 2:
        col = 0
        row += 1

root.mainloop()
