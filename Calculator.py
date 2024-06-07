import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function to update the entry field with button presses
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry field
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=4, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons and place them in the grid
row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: button_click(x) if x != '=' else evaluate_expression()
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, bd=8, font=('Arial', 18), command=action)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, bd=8, font=('Arial', 18), command=action)
    btn.grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add a clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, bd=8, font=('Arial', 18), command=clear_entry)
clear_button.grid(row=row_val, column=0, columnspan=4, sticky='we')

# Run the application
root.mainloop()
