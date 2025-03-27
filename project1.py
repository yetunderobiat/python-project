import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()  # Get value from the name entry widget
    email =  email_entry.get()      # Get value from the email entry widget

    # Check if all fields are filled
    if name and email:
        # print the information to the  console(you can process the data as needed)
        print(f"Name: {name}")
        print(f"Email: {email}")
        # Show a success  message box
        messagebox.showinfo("Form submitted", "Your information has been submitted successfully!")

    else:
        # show an error message if any field is empty
        messagebox.showerror("Error", "Please fill in all fields.")


# Create the main window
root = tk.Tk()
root.title("User Registration Form")

# Set the window size
root.geometry("400x250")

# Create a label and entry for name
name_label = tk.Label(root,text="Name:")        # Create label for the name field
name_label.grid(row=0, column=0, padx=10, pady=10)      # Place the label on the grid

name_entry = tk.Entry(root)     # create label for the name field
name_entry.grid(row=0, column=1, padx=10, pady=10)      # place the entry field next to the label

# Create a label and entry for email
email_label = tk.Label(root,text="Email:")        # Create label for the email field
email_label.grid(row=1, column=0, padx=10, pady=10)      # Place the label on the grid

email_entry = tk.Entry(root)     # Create label for the email field
email_entry.grid(row=1, column=1, padx=10, pady=10)      # Place the entry field next to the label

# Create a submit button that will trigger the form submission
submit_button = tk.Button(root, text="Submit", command=submit_form)     # Button will call submit_form function
submit_button.grid(row=2,  columnspan=2, pady=20)       # Place the button below the fields

# Start the GUI event loop
root.mainloop()





