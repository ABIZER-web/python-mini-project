import tkinter as tk
from tkinter import ttk

class MillionaireTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AA ")
        self.root.geometry("600x600")
        self.root.configure(bg="#2c3e50")  # Dark grey background

        # Notebook (Tabs)
        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill="both")

        # Create Frames for Tabs
        home_frame = tk.Frame(notebook, bg="#2c3e50")
        support_frame = tk.Frame(notebook, bg="#2c3e50")

        notebook.add(home_frame, text="Home")
        notebook.add(support_frame, text="Support")

        # Home Page Content
        self.add_home_content(home_frame)

        # Support Page Content
        self.add_support_content(support_frame)

    def add_home_content(self, frame):
        title = tk.Label(frame, text="Welcome to AA", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
        title.pack(pady=10)

        description = tk.Label(frame, text=(
            "If you’re seeking a successful career and a lifetime of happiness, you’ve come to the right place. "
            "At AA Private Limited, we offer the finest learning experience and unparalleled growth opportunities."
        ), font=("Arial", 12), fg="white", bg="#2c3e50", wraplength=550, justify="center")
        description.pack(pady=5)

        approach = tk.Label(frame, text="Our Smart Approach: Combining diligence with innovative strategies.", 
                            font=("Arial", 12, "italic"), fg="white", bg="#2c3e50")
        approach.pack(pady=5)

        # Why Choose Us
        why_label = tk.Label(frame, text="Why Choose Us?", font=("Arial", 14, "bold"), fg="yellow", bg="#2c3e50")
        why_label.pack(pady=10)

        reasons = [
            "✔ Expert Instructors: Learn from the best.",
            "✔ Flexible Learning: Study at your own pace.",
            "✔ Affordable Pricing: Quality education at low cost.",
            "✔ Supportive Community: Connect with learners worldwide."
        ]
        for reason in reasons:
            lbl = tk.Label(frame, text=reason, font=("Arial", 12), fg="white", bg="#2c3e50")
            lbl.pack(anchor="w", padx=20)

        # Call to Action
        call_to_action = tk.Label(frame, text="Join AA today and transform your career!",
                                  font=("Arial", 12, "bold"), fg="lightgreen", bg="#2c3e50", pady=10)
        call_to_action.pack()

    def add_support_content(self, frame):
        title = tk.Label(frame, text="Support & Policies", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
        title.pack(pady=10)

        support_links = [
            "About Us", "Gallery", "Career", "Become An Instructor", "Login"
        ]
        for link in support_links:
            lbl = tk.Label(frame, text=f"• {link}", font=("Arial", 12), fg="white", bg="#2c3e50")
            lbl.pack(anchor="w", padx=20)

        policies_label = tk.Label(frame, text="Our Policies:", font=("Arial", 14, "bold"), fg="yellow", bg="#2c3e50")
        policies_label.pack(pady=10)

        policies = ["Refund Policy", "Terms & Conditions", "Disclaimer", "Privacy Policy"]
        for policy in policies:
            lbl = tk.Label(frame, text=f"✔ {policy}", font=("Arial", 12), fg="white", bg="#2c3e50")
            lbl.pack(anchor="w", padx=20)

        # Footer
        footer = tk.Label(frame, text="All Rights Reserved © 2025 | AA Pvt. Ltd.",
                          font=("Arial", 10), fg="lightgray", bg="#2c3e50")
        footer.pack(pady=20)

# Run the Tkinter App
if __name__ == "__main__":
    root = tk.Tk()
    app = MillionaireTrackApp(root)
    root.mainloop()
