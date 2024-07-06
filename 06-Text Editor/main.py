import tkinter as tk
from tkinter import filedialog as tkf

#file manage
def open_file():
    file_path= tkf.askopenfilename(
    filetypes =[('Text Files', '*.txt'), ("All Files", "*.*")]
    )
    if file_path is not None:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                txt_edit.delete(1.0, tk.END)
                txt_edit.insert(tk.END, content)
            window.title(f'Text Editor - {file_path}')
        except IOError as err:
            print(f"Error reading the file: {err}")

def save_file():
    file_path = tkf.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            content = txt_edit.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            window.title(f'Text Editor - {file_path}')
        except IOError as err:
            print(f"Error saving to the file: {err}")
            
#username
user = input("Enter your name: ")

#main
window = tk.Tk()
window.title("Text Editor")
window.minsize(width=660, height=470)

#widgets
txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save File", command=save_file)

#label
greeting = tk.Label(window, text=f"Hello, {user}")

#layout
greeting.grid(column=0, row=0, sticky="w", padx=5, pady=5)

btn_open.grid(column=1, row=0, sticky="ew", padx=5, pady=5)
btn_save.grid(column=2, row=0, sticky="ew", padx=5, pady=5)
frame_buttons.grid(column=0, row=1, columnspan=3, sticky="ew")

txt_edit.grid(column=0, row=2, columnspan=3, sticky="nsew")

#run
window.mainloop()
