# using Tkinker to create a python gui app
# first Name
# last name 
# email
# phone number
# gender

import tkinter as tk
from tkinter import messagebox

def submit_form():
    firstName = firstName_entry.get()
    lastName = lastName_entry.get()
    email = email_entry.get()
    phoneNumber = phoneNumber_entry.get()
    gender  = gender_var.get()

    if firstName and lastName and email and phoneNumber and gender:
        print(f"First Name: {firstName}")
        print(f"Last Name: {lastName}")
        print(f"Email: {email}")
        print(f"Phone Number: {phoneNumber}")
        print(f"Gender: {gender}")

        messagebox.showinfo("You have sucessfully submitted")
    else:
        messagebox.showerror("Wrong input. Try again")

root = tk.Tk()
root.title("My registration form")
root.geometry("300x250")

firstName_label = tk.Label(root,text = "First Name:")
firstName_label.grid(row=0, column=0, padx=10, pady=10)

firstName_entry = tk.Entry(root)
firstName_entry.grid(row=0, column=1, padx=10, pady=10)

lastName_label = tk.Label(root,text = "Last Name:")
lastName_label.grid(row=1, column=0, padx=10, pady=10)

lastName_entry = tk.Entry(root)
lastName_entry.grid(row=1, column=1, padx=10, pady=10)

email_label = tk.Label(root,text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10)

email_entry = tk.Entry(root)
email_label.grid(row=2, column=1, padx=10, pady=10)

phoneNumber_label = tk.Label(root,text = "Phone number:")
phoneNumber_label.grid(row=3, column=0, padx=10, pady=10)

phoneNumber_entry = tk.Entry(root)
phoneNumber_entry.grid(row=3, column=1, padx=10, pady=10)

# gender = tk.StringVar(value="Male")
# male_radio = tk.Radiobutton(root, text="Male", variable=gender, value="Male")
# female_radio = tk.Radiobutton(root, text="Female", variable=gender, value="Female")
# other_radio = tk.Radiobutton(root, text="Other", variable=gender, value="Other")

# male_radio.pack(anchor='w')
# female_radio.pack(anchor='w')
# other_radio.pack(anchor='w')
gender_var = tk.Label(root,text="Gender:")
gender_var.grid(row=4, column=0, padx=10, pady=10)
gender_var = tk.StringVar(value="Not Specified")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

show_button = tk.Button(root, text="Show selection", command=submit_form)
show_button.pack()
# gender_label = tk.Label(root,text="Gender:")
# gender_label.grid(row=4, column=0, padx=10, pady=10)

# gender_entry = tk.Entry(root)
# gender_entry.grid(row=4, column=1, padx=10, pady=10)
        
# tk.Button(root, text="Submit", command=submit_form).pack(pady=10)
submit_button = tk.Button(root, text="Submit", command=submit_form)    
submit_button.grid(row=5,  columnspan=3, padx=10, pady=10)

root.mainloop()

