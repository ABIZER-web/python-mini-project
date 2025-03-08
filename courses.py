import tkinter as tk
from tkinter import ttk

# Function to display course details in a scrollable GUI
def show_courses():
    root = tk.Tk()
    root.title("Courses")
    root.geometry("500x400")

    # Create a frame and canvas for scrolling
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack canvas and scrollbar
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # List of courses
    courses = [
        {"title": "Instagram Marketing", "description": "Instagram is one of the most trending and fastest growing platforms...", "lessons": 10, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Canva", "description": "Canva is empowering with its creative tools...", "lessons": 15, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Communication Skills", "description": "Communication is not just speaking; it is more than that...", "lessons": 15, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Instagram Reels Mastery", "description": "Instagram reels mastery is the best way to grow...", "lessons": 18, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Adobe Premiere Pro", "description": "Video Editing is one of the most demanding careers...", "lessons": 16, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Adobe Photoshop", "description": "Photoshop offers you a limitless opportunity to grow...", "lessons": 14, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Google Ads", "description": "Google Ads, an advertising platform, is leading the world...", "lessons": 93, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Facebook Ads", "description": "Facebook Ads are an effective way to drive traffic from active users as it is a budget-friendly platform...", "lessons": 30, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "LinkedIn Marketing", "description": "If you are looking to build your career in the Digital marketing industry there is no better time than now...", "lessons": 40, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Microsoft Ads", "description": "Microsoft ads are building smarter journeys to build customer awareness of your business brand...", "lessons": 64, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "YouTube Marketing", "description": "If you are looking to build your career in the Digital marketing industry there is no better time than now...", "lessons": 24, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Email Marketing", "description": "Email Marketing is the most powerful marketing channel playing a pivotal role to foster the value of your brand and building a fast effective way to reach out to new potential customers...", "lessons": 12, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Stock Market", "description": "Investment in Stock Market is a great way to build wealth. To become a successful investor educating yourself about the Stock Market is important...", "lessons": 31, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Option Trading", "description": "Since the return is higher it has been becoming more popular nowadays here, you will develop a strategy for options trading because you need to be careful while trading...", "lessons": 17, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Power BI", "description": "POWER BI is a powerful analytical tool that helps companies of all sizes to analyze data and share insights...", "lessons": 18, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Machine Learning", "description": "Machine learning vows to solve problems and benefits the company by helping them to make better decisions...", "lessons": 0, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"},
        {"title": "Python", "description": "Python is an in-demand high-level programming language. The easy-to-learn language provides increased productivity to programmers...", "lessons": 49, "students_enrolled": "2 Lakh+", "certificate": "Millionaire Track Certificate", "action": "Explore Now"}
    ]
    
    # Display courses
    for course in courses:
        frame = tk.Frame(scrollable_frame, borderwidth=2, relief="solid", padx=5, pady=5)
        frame.pack(padx=10, pady=5, fill="x")
        
        tk.Label(frame, text=f"Title: {course['title']}", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(frame, text=f"Description: {course['description']}", wraplength=400, justify="left").pack(anchor="w")
        tk.Label(frame, text=f"Lessons: {course['lessons']}").pack(anchor="w")
        tk.Label(frame, text=f"Students Enrolled: {course['students_enrolled']}").pack(anchor="w")
        tk.Label(frame, text=f"Certificate: {course['certificate']}").pack(anchor="w")
        tk.Label(frame, text=f"Action: {course['action']}", fg="blue").pack(anchor="w")
    
    root.mainloop()

# Run the function to display courses
show_courses()