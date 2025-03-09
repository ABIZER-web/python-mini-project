import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def open_course_window(course):
    course_window = tk.Toplevel()
    course_window.title(course['title'])
    course_window.geometry("500x600")
    
    lesson_frame = tk.Frame(course_window)
    lesson_frame.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(lesson_frame)
    scrollbar = ttk.Scrollbar(lesson_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    for i in range(course['lessons']):
        tk.Label(scrollable_frame, text=f"Lesson {i+1}", font=("Arial", 12, "bold"), relief="solid", padx=5, pady=5).pack(pady=2, fill="x")
    
    mentor_frame = tk.Frame(course_window, relief="solid", borderwidth=2)
    mentor_frame.pack(fill=tk.X, pady=10)
    
    mentor_label = tk.Label(mentor_frame, text="Mentor", font=("Arial", 14, "bold"))
    mentor_label.pack()
    
    try:
        mentor_image = Image.open("mentor.jpg")
        mentor_image = mentor_image.resize((100, 100), Image.ANTIALIAS)
        mentor_photo = ImageTk.PhotoImage(mentor_image)
        
        mentor_pic = tk.Label(mentor_frame, image=mentor_photo)
        mentor_pic.image = mentor_photo
        mentor_pic.pack()
    except Exception as e:
        tk.Label(mentor_frame, text="[Image Not Available]", font=("Arial", 10, "italic"), fg="red").pack()
    
    mentor_info = tk.Label(mentor_frame, text="Dr. John Doe\nPhD in Digital Marketing", font=("Arial", 12))
    mentor_info.pack()

def show_courses():
    root = tk.Tk()
    root.title("Courses")
    root.geometry("500x400")
    
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    courses = [
        {"title": "Instagram Marketing", "description": "Learn Instagram growth strategies", "lessons": 10},
        {"title": "Python", "description": "Master Python programming", "lessons": 49},
        {"title": "Adobe Photoshop", "description": "Become a pro at photo editing", "lessons": 14},
        {"title": "Machine Learning", "description": "Dive into AI and ML concepts", "lessons": 20},
        {"title": "Google Ads", "description": "Run successful Google ad campaigns", "lessons": 30},
        {"title": "Canva", "description": "Master Canva for creative design", "lessons": 15},
        {"title": "Communication Skills", "description": "Improve your communication skills", "lessons": 15},
        {"title": "Instagram Reels Mastery", "description": "Learn to grow using Instagram Reels", "lessons": 18},
        {"title": "Adobe Premiere Pro", "description": "Video editing mastery with Premiere Pro", "lessons": 16},
        {"title": "Facebook Ads", "description": "Run effective Facebook ad campaigns", "lessons": 30},
        {"title": "LinkedIn Marketing", "description": "Boost your career with LinkedIn strategies", "lessons": 40},
        {"title": "Microsoft Ads", "description": "Use Microsoft Ads for business growth", "lessons": 64},
        {"title": "YouTube Marketing", "description": "Market effectively on YouTube", "lessons": 24},
        {"title": "Email Marketing", "description": "Leverage email for marketing success", "lessons": 12},
        {"title": "Stock Market", "description": "Learn the fundamentals of stock trading", "lessons": 31},
        {"title": "Option Trading", "description": "Develop a strategy for options trading", "lessons": 17},
        {"title": "Power BI", "description": "Analyze and visualize data with Power BI", "lessons": 18}
    ]
    
    for course in courses:
        frame = tk.Frame(scrollable_frame, borderwidth=2, relief="solid", padx=5, pady=5)
        frame.pack(padx=10, pady=5, fill="x")
        
        tk.Label(frame, text=f"Title: {course['title']}", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(frame, text=f"Description: {course['description']}", wraplength=400, justify="left").pack(anchor="w")
        
        explore_button = tk.Button(frame, text="Explore Now", fg="blue", command=lambda c=course: open_course_window(c))
        explore_button.pack(anchor="w")
    
    root.mainloop()
    
show_courses()
