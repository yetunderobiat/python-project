import tkinter as tk
from tkinter import messagebox

def submit_form():
    fullName = fullName_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    country = country_entry.get()
    programming = programming_var.get()

    if fullName and email and gender and country and programming:
        print(f"Full Name: {fullName}")
        print(f"Email: {email}")
        print(f"Gender: {gender}")
        print(f"Country: {country}")
        print(f"Programming: {programming}")

        messagebox.showinfo("Form Submitted", "Your information has been recorded.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

root = tk.Tk()
root.title('Registration Form')
root.geometry('500x500')

# Full Name
tk.Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
fullName_entry = tk.Entry(root)
fullName_entry.grid(row=0, column=1, padx=10, pady=10)

# Email
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Gender
tk.Label(root, text="Select Gender:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
gender_var = tk.StringVar()
genders = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
for i, (text, value) in enumerate(genders):
    tk.Radiobutton(root, text=text, variable=gender_var, value=value).grid(row=2, column=1+i, sticky='w')

# Country
tk.Label(root, text="Country:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
country_entry = tk.Entry(root)
country_entry.grid(row=3, column=1, padx=10, pady=10)

# Programming Language
tk.Label(root, text="Select Program:").grid(row=4, column=0, padx=10, pady=10, sticky='w')
programming_var = tk.StringVar()
programs = [("Java", "Java"), ("Python", "Python")]
for i, (text, value) in enumerate(programs):
    tk.Radiobutton(root, text=text, variable=programming_var, value=value).grid(row=4, column=1+i, sticky='w')

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
