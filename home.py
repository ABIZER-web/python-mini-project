import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

def show_home():
    messagebox.showinfo("Home", "Welcome to the Home Page!")

def show_courses():
    subprocess.Popen(["python", "courses.py"])  # Redirects to courses.py

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
root.attributes('-fullscreen', True)  # Fullscreen mode

# Load the background image
image_path = "marketing.jpeg"  # Use the correct path
bg_image = Image.open(image_path)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)  # Resize image to fit full screen
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas and set the background
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create and place navigation buttons on the canvas
button_frame = tk.Frame(root, bg="white")  # Frame for buttons
button_frame.place(relx=0.5, rely=0.05, anchor="n")  # Positioned at the top

buttons = [
    ("Home", show_home),
    ("Courses", show_courses),
    ("About Us", show_about_us),
    ("Contact Us", show_contact_us),
    ("Enroll", enroll),
    ("Login", show_login)
]

for i, (text, command) in enumerate(buttons):
    btn = tk.Button(button_frame, text=text, command=command, bg="white", fg="black", font=("Arial", 14, "bold"), padx=10, pady=5)
    btn.grid(row=0, column=i, padx=15, pady=10)

# Exit on pressing Escape
def exit_fullscreen(event):
    root.destroy()
root.bind("<Escape>", exit_fullscreen)

# Start the main event loop
root.mainloop()
