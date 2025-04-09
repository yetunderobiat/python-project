import tkinter as tk
from tkinter import messagebox

def submit_form():
    fullName = fullName_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    country = messagebox.showinfo("Select your country")
    programming = programming_var.get()

    if fullName and  email and gender and country and programming:
        print(f"Full Name: {fullName}")
        print(f"Email: {email}")
        print(f"Gender: {gender}")
        print(f"Country: {country}")
        print(f"Programming: {programming}")

        messagebox.showinfo("Form submitted successfully", "Your information has been recorded")

    else:
        
        messagebox.showerror("Error", "Please fill in all fields.")

    