import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import webbrowser
import sqlite3

# List of random video URLs
video_links = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=3JZ_D3ELwOQ",
    "https://www.youtube.com/watch?v=2vjPBrBU-TM",
    "https://www.youtube.com/watch?v=LXb3EKWsInQ",
    "https://www.youtube.com/watch?v=KMU0tzLwhbE"
]

# Initialize database for progress tracking
conn = sqlite3.connect("aa.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS progress (course TEXT, lesson INTEGER, completed INTEGER)")
conn.commit()

def update_progress(course, lesson):
    c.execute("INSERT OR REPLACE INTO progress (course, lesson, completed) VALUES (?, ?, 1)", (course, lesson))
    conn.commit()

def generate_certificate(course):
    cert_window = tk.Toplevel()
    cert_window.title("Certificate")
    tk.Label(cert_window, text=f"Congratulations! You completed {course}", font=("Arial", 14, "bold")).pack(pady=20)

def open_course_window(course):
    course_window = tk.Toplevel()
    course_window.title(course['title'])
    course_window.geometry("600x700")
    
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
        lesson_container = tk.Frame(scrollable_frame, relief="solid", borderwidth=2, padx=5, pady=5)
        lesson_container.pack(pady=5, fill="x")
        
        lesson_label = tk.Label(lesson_container, text=f"Lesson {i+1}", font=("Arial", 12, "bold"))
        lesson_label.pack(anchor="w")
        
        video_url = random.choice(video_links)
        play_button = tk.Button(lesson_container, text="Play Video", command=lambda url=video_url: webbrowser.open(url), fg="blue")
        play_button.pack(pady=5)
        
        complete_button = tk.Button(lesson_container, text="Mark Complete", command=lambda c=course['title'], l=i+1: update_progress(c, l), fg="green")
        complete_button.pack(pady=5)
    
    cert_button = tk.Button(course_window, text="Generate Certificate", command=lambda c=course['title']: generate_certificate(c), fg="purple")
    cert_button.pack(pady=10)
    
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
    except Exception:
        tk.Label(mentor_frame, text="[Image Not Available]", font=("Arial", 10, "italic"), fg="red").pack()
    
    mentor_info = tk.Label(mentor_frame, text="Dr. John Doe\nPhD in Online Marketing", font=("Arial", 12))
    mentor_info.pack()

def show_courses():
    root = tk.Tk()
    root.title("Online Marketing Courses")
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
        {"title": "Instagram Reels Mastery", "description": "Learn to grow using Instagram Reels", "lessons": 18},
        {"title": "LinkedIn Marketing", "description": "Boost your career with LinkedIn strategies", "lessons": 40},
        {"title": "YouTube Marketing", "description": "Market effectively on YouTube", "lessons": 24},
        {"title": "Email Marketing", "description": "Leverage email for marketing success", "lessons": 12}
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
