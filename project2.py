import tkinter as tk
from tkinter import messagebox


def submit_form():
    firstName = firstName_entry.get()  
    lastName = lastName_entry.get() 
    email =  email_entry.get()      

    if firstName and lastName and email:
        print(f"First Name: {firstName}")
        print(f"Last Name: {lastName}")
        print(f"Email: {email}")

        messagebox.showinfo("Form submitted", "Your information has been submitted successfully!")

    else:
        messagebox.showerror("Error", "Please fill in all fields.")


root = tk.Tk()
root.title("User Registration Form")

root.geometry("400x250")

firstName_label = tk.Label(root,text="First Name:")       
firstName_label.grid(row=0, column=0, padx=10, pady=10)      

firstName_entry = tk.Entry(root)    
firstName_entry.grid(row=0, column=1, padx=10, pady=10)      

lastName_label = tk.Label(root,text="Last Name:")        
lastName_label.grid(row=1, column=0, padx=10, pady=10)      

lastName_entry = tk.Entry(root)     
lastName_entry.grid(row=1, column=1, padx=10, pady=10)     

email_label = tk.Label(root,text="Email:")       
email_label.grid(row=2, column=0, padx=10, pady=10)      

email_entry = tk.Entry(root)    
email_entry.grid(row=2, column=1, padx=10, pady=10)     


submit_button = tk.Button(root, text="Submit", command=submit_form)    
submit_button.grid(row=3,  columnspan=3, padx=10, pady=10)

root.mainloop()