import tkinter as tk
from tkinter import messagebox

def display_info():
    user_input = entry_input.get()
    name = entry_name.get()
    age = entry_age.get()
    color = entry_color.get()
    messagebox.showinfo("Information", f"You entered: {user_input}\nHello, {name}! You are {age} years old and your favorite color is {color}.")

# Create the main window
root = tk.Tk()
root.title("User Information")

# Create and place the widgets
tk.Label(root, text="Please enter something:").grid(row=0, column=0)
entry_input = tk.Entry(root)
entry_input.grid(row=0, column=1)

tk.Label(root, text="Please enter your name:").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Please enter your age:").grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

tk.Label(root, text="Please enter your favorite color:").grid(row=3, column=0)
entry_color = tk.Entry(root)
entry_color.grid(row=3, column=1)

tk.Button(root, text="Submit", command=display_info).grid(row=4, columnspan=2)

# Run the application
root.mainloop()