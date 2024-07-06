import tkinter as tk

user=input("enter your name: ")

window = tk.Tk()
window.title("Text Editor")
window.minsize(width=725, height=400)

txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open File")
btn_save = tk.Button(frame_buttons, text="Save File")

btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
btn_save.grid(column=0, row=1, sticky="ew", padx=5)

txt_edit.grid(column=1, row=0, sticky="nsew")
frame_buttons.grid(column=0, row=0, sticky="ns")

greeting = tk.Label(text=f"Hello,{user}")
print(greeting)

window.mainloop()