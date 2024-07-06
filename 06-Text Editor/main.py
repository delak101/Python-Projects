import tkinter as tk

# Getting user input
user = input("Enter your name: ")

# Creating the main window
window = tk.Tk()
window.title("Text Editor")
window.minsize(width=725, height=400)

# Creating widgets
txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open File")
btn_save = tk.Button(frame_buttons, text="Save File")

# Placing widgets using grid layout
btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
btn_save.grid(column=1, row=0, sticky="ew", padx=5, pady=5)
frame_buttons.grid(column=0, row=0, sticky="ns")
txt_edit.grid(column=1, row=1, columnspan=2, sticky="nsew")

# Creating and placing the greeting label
greeting = tk.Label(window, text=f"Hello, {user}")
greeting.grid(column=0, row=1, pady=10)

# Running the main event loop
window.mainloop()
