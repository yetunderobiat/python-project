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

# code explanation 
# 1. import tkinter as tk: tkinter is a python library for creating graphical user interfaces(GUI). we import it to use its tools and widgets for our calculator.
# 2. function: click_button (value): this function is called when the user clicks any button on the calculator(like ,7,8).
# clear() this function clears theinput area when the user clicks the C button.
# calculate() this function is used when the user clicks the '=' button. it itakes the maths expression the userenntered and calculate the result using python's eval() function.
# 3. creating the main window: root=tk.Tk(). this line creates the main window (the box where everything will appear). root.title('Simple calculator), which will appear at the top of the win
# 4. creating the entry widget(display area): entry=tk.Entry(...)
#this creates a box(called an 'entry' widget) where the use will see the numbers they type. it's like the screen of a calculator where the result is  shown.
# the font=('arial',24)part setsthe text size to make it easy to read. 
# the justify right part makes sure the numbers appear on the right side of the entry box.
# 6. button layout: button=[..] this is a list that comtains the names of the button
# button = tk.Button this line creates a button for each items in the list. 
# 7.  placing buttons in the grid. button.grid(row=row, column=col): this places each button in the window at the specified row and column
# 8. running the syste root.mainloop(): this tells the program to keep the window open and wair for user interaction(like button click). without this line, the  window would open and close
