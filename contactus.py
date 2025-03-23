import tkinter as tk
from tkinter import messagebox

class ContactInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Information")
        self.root.geometry("400x400")
        self.root.configure(bg="#2c3e50")  # Dark grey background

        # Title Label
        title_label = tk.Label(root, text="Get in Touch", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
        title_label.pack(pady=10)

        # Description Label
        desc_label = tk.Label(root, text="Please feel free to talk to us if you have any questions.",
                              font=("Arial", 12), fg="white", bg="#2c3e50", wraplength=350)
        desc_label.pack(pady=5)

        # Contact Form
        self.name_entry = self.create_input_field("Your Name:")
        self.phone_entry = self.create_input_field("Phone:")
        self.message_entry = self.create_input_field("Message:")

        # Submit Button
        submit_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"),
                                  bg="#27ae60", fg="white", command=self.submit_form)
        submit_button.pack(pady=10)

        # Support Contact
        contact_label = tk.Label(root, text="Support Contact:", font=("Arial", 14, "bold"), fg="white", bg="#2c3e50")
        contact_label.pack(pady=5)

        # Phone Numbers
        phone_label = tk.Label(root, text="+91 9004659297\n+91 7426825253",
                               font=("Arial", 12), fg="white", bg="#2c3e50")
        phone_label.pack()

        # Email
        email_label = tk.Label(root, text="Email: alisha270105@gmail.com", font=("Arial", 12), fg="white", bg="#2c3e50")
        email_label.pack()

        # Address
        address_label = tk.Label(root, text="Address: K.K Residency G-Wing, 502,\nAzad Nagar, Ghatkopar West",
                                 font=("Arial", 12), fg="white", bg="#2c3e50", wraplength=350)
        address_label.pack(pady=5)

    def create_input_field(self, label_text):
        frame = tk.Frame(self.root, bg="#2c3e50")
        frame.pack(pady=5)
        label = tk.Label(frame, text=label_text, font=("Arial", 12), fg="white", bg="#2c3e50")
        label.pack(side="left", padx=5)
        entry = tk.Entry(frame, font=("Arial", 12), width=25)
        entry.pack(side="right", padx=5)
        return entry

    def submit_form(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        message = self.message_entry.get()

        if name and phone and message:
            messagebox.showinfo("Success", "Your message has been sent successfully!")
        else:
            messagebox.showerror("Error", "Please fill all fields before submitting.")

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactInfoApp(root)
    root.mainloop()
