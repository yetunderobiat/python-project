import tkinter as tk 

# function to perform the calculation
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
        entry.insert(0, 'Error')

# create the main window
root = tk.Tk()
root.title('Simple Calculation')

# create the entry widget for showing the current input/output
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

#  Button layout and creation
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 6, 3), ('D', 5, 3)
           ] 

# create each button and place it in the grid
for(text, row, col)in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=clear)
    elif text == 'D':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda
        value = text: click_button(value))
        button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()

# code explanation 
# 1. import tkinter as tk: