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
root.title("Registration Form")
root.geometry('600x700')
root.configure(bg="lightblue") 

# Registration form
root.title_label = tk.Label(root, text="Registration Form", font=("Arial", 22, "bold"), width=20, background= 'lightblue')
root.title_label.grid(row=0, column=0, columnspan=2, pady=(40, 20))

# Full Name
fullName_label = tk.Label(root,text="Full Name:", font=("Times New Roman", 14, "bold"), background= 'lightblue')       
fullName_label.grid(row=1, column=0, padx=30, pady=30)

fullName_entry = tk.Entry(root)
fullName_entry.grid(row=1, column=1, padx=30, pady=30)

# Email
email_label = tk.Label(root,text="Email:", font=("Times New Roman", 14, "bold"), background= 'lightblue')
email_label.grid(row=2, column=0, padx=30, pady=30)

email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=30, pady=30)

# Gender
gender_var = tk.Label(root, text="Select Gender:", font=("Times New Roman", 14, "bold"), background= 'lightblue')
gender_var.grid(row=3, column=0, padx=30, pady=30)
gender_var = tk.StringVar()

genders = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
for i, (text, value) in enumerate(genders):
    tk.Radiobutton(root, text=text, variable=gender_var, value=value).grid(row=3, column=1+i)

# Country
country_entry = tk.Label(root, text="Country:", font=("Times New Roman", 14, "bold"), background= 'lightblue')
country_entry.grid(row=4, column=0, padx=30, pady=30)

country_entry = tk.Entry(root)
country_entry.grid(row=4, column=1, padx=30, pady=30)

# Programming 
programming_var = tk.Label(root, text="Select Program:", font=("Times New Roman", 14, "bold"), background= 'lightblue')
programming_var.grid(row=5, column=0, padx=30, pady=30)

programming_var = tk.StringVar()
programs = [("Java", "Java"), ("Python", "Python")]
for i, (text, value) in enumerate(programs):
    tk.Radiobutton(root, text=text, variable=programming_var, value=value).grid(row=5, column=1+i)

# Submit Button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), width=30, borderwidth=2, background='red', command=submit_form)
submit_button.grid(row=6, column=0, columnspan=3, pady=30)

root.mainloop()
