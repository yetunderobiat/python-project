# import tkinter as tk

 

# # Function to perform the calculations

# def click_button(value):

#     current = entry.get()

#     entry.delete(0, tk.END)

#     entry.insert(0, current + value)

 

# def clear():

#     entry.delete(0, tk.END)

 

# def calculate():

#     try:

#         result = eval(entry.get())

#         entry.delete(0, tk.END)

#         entry.insert(0, result)

#     except:

#         entry.delete(0, tk.END)

#         entry.insert(0, "Error")

 

# # Create the main window

# root = tk.Tk()

# root.title("Simple Calculator")

 

# # Create the entry widget for showing the current input/output

# entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")

# entry.grid(row=0, column=0, columnspan=4)

 

# # Button layout and creation

# buttons = [

#     ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),

#     ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),

#     ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),

#     ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),

#     ("C", 5, 0)

# ]

 

# # Create each button and place it in the grid

# for (text, row, col) in buttons:

#     if text == "=":

#         button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)

#     elif text == "C":

#         button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)

#     else:

#         button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: click_button(value))

   

#     button.grid(row=row, column=col, padx=5, pady=5)

 

# # Run the main loop

# root.mainloop()
import tkinter as tk

# Function to perform the calculations
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#e0e0e0")  # Light gray background

# Create the entry widget
root.title_label = tk.Label(root, text="Simple Calculator", font=("Arial", 22, "bold"), bg="#e0e0e0")
root.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="white", fg="black")
entry.grid(row=1, column=1, columnspan=3, padx=15, pady=15)



# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create each button and place it
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
        command=calculate, bg="#4CAF50", fg="white")  # Green
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
        command=clear, bg="#f44336", fg="white")  # Red
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
        command=lambda value=text: click_button(value), bg="#424242", fg="white")  # Dark gray

    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()


