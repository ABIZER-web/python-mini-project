import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import ttkbootstrap as ttk  # Import ttkbootstrap
from ttkbootstrap.constants import *

class HeadlineApp:
    def __init__(self, parent):
        self.parent = parent
        self.headline_texts = ["Elevate your brand", "Increase Sales", "Inspire audiences"]
        self.headline_index = 0
        self.headline_label = tk.Label(parent, text=self.headline_texts[self.headline_index], fg="white", bg="black", font=("Arial", 20, "bold"))
        self.headline_label.place(relx=0.5, rely=0.12, anchor="center")  # Positioned below buttons
        self.update_headline()
    
    def update_headline(self):
        self.headline_index = (self.headline_index + 1) % len(self.headline_texts)
        self.headline_label.config(text=self.headline_texts[self.headline_index])
        self.parent.after(2000, self.update_headline)

# Create the main window
root = ttk.Window(themename="superhero")  # Using ttkbootstrap theme
root.title("Home Page")
root.attributes('-fullscreen', True)

# Load the background image
image_path = "marketing (1).png"
bg_image = Image.open(image_path)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas and set the background
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create and place navigation buttons with ttkbootstrap styling
button_frame = ttk.Frame(root)
button_frame.place(relx=0.5, rely=0.05, anchor="n")

buttons = [
    ("Home", lambda: messagebox.showinfo("Home", "Welcome to the Home Page!"), "secondary"),
    ("Courses", lambda: subprocess.Popen(["python", "courses.py"]), "secondary"),
    ("About Us", lambda: subprocess.Popen(["python", "aboutus.py"]), "secondary"),  # Updated
    ("Contact Us", lambda: subprocess.Popen(["python", "contactus.py"]), "secondary"),  # Updated
    ("Enroll Now", lambda: subprocess.Popen(["python", "enroll.py"]), "warning"),
    ("Login", lambda: subprocess.Popen(["python", "login.py"]), "outline-warning")
]


for i, (text, command, style) in enumerate(buttons):
    btn = ttk.Button(button_frame, text=text, command=command, bootstyle=style, padding=(15, 8))
    btn.grid(row=0, column=i, padx=20, pady=10)  # Increased spacing

# Add Headline Feature
headline_app = HeadlineApp(root)

# Exit on pressing Escape
def exit_fullscreen(event):
    root.destroy()
root.bind("<Escape>", exit_fullscreen)

# Start the main event loop
root.mainloop()
