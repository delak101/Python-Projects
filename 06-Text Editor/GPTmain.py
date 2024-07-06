import tkinter as tk
from tkinter import filedialog as tkf
from tkinter import messagebox

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Editor")
        self.geometry("660x470")

        self.create_widgets()

        # Initialize variables
        self.file_path = None

    def create_widgets(self):
        # Text widget for editing
        self.txt_edit = tk.Text(self, wrap=tk.WORD)
        self.txt_edit.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Scrollbar
        scroll_bar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.txt_edit.yview)
        scroll_bar.grid(row=1, column=4, sticky="ns")
        self.txt_edit.config(yscrollcommand=scroll_bar.set)

        # Frame for buttons
        frame_buttons = tk.Frame(self)
        frame_buttons.grid(row=0, column=0, columnspan=4, sticky="ew")

        # Buttons for file operations, formatting, word count, and exit
        self.create_button(frame_buttons, "Open File", self.open_file)
        self.create_button(frame_buttons, "Save File", self.save_file)
        self.create_button(frame_buttons, "Bold", self.toggle_bold)
        self.create_button(frame_buttons, "Italic", self.toggle_italic)
        self.create_button(frame_buttons, "Underline", self.toggle_underline)
        self.create_button(frame_buttons, "Word Count", self.count_words)
        self.create_button(frame_buttons, "Exit", self.exit_editor)

    def create_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, command=command)
        btn.grid(padx=5, pady=5)
        return btn

    def open_file(self):
        self.file_path = tkf.askopenfilename(
            filetypes=[('Text Files', '*.txt'), ("All Files", "*.*")]
        )
        if self.file_path:
            try:
                with open(self.file_path, 'r') as file:
                    content = file.read()
                    self.txt_edit.delete(1.0, tk.END)
                    self.txt_edit.insert(tk.END, content)
                self.title(f'Text Editor - {self.file_path}')
            except IOError as err:
                messagebox.showerror("Error", f"Error reading the file: {err}")

    def save_file(self):
        if self.file_path:
            try:
                content = self.txt_edit.get(1.0, tk.END)
                with open(self.file_path, 'w') as file:
                    file.write(content)
                self.title(f'Text Editor - {self.file_path}')
            except IOError as err:
                messagebox.showerror("Error", f"Error saving to the file: {err}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = tkf.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                content = self.txt_edit.get(1.0, tk.END)
                with open(file_path, 'w') as file:
                    file.write(content)
                self.file_path = file_path
                self.title(f'Text Editor - {self.file_path}')
            except IOError as err:
                messagebox.showerror("Error", f"Error saving to the file: {err}")

    def toggle_bold(self):
        self.toggle_tag("bold", "bold")

    def toggle_italic(self):
        self.toggle_tag("italic", "italic")

    def toggle_underline(self):
        self.toggle_tag("underline", underline=True)

    def toggle_tag(self, tag_name, **kwargs):
        current_tags = self.txt_edit.tag_names("sel.first")
        if tag_name in current_tags:
            self.txt_edit.tag_remove(tag_name, "sel.first", "sel.last")
        else:
            self.txt_edit.tag_add(tag_name, "sel.first", "sel.last")
            self.txt_edit.tag_configure(tag_name, **kwargs)

    def count_words(self):
        content = self.txt_edit.get(1.0, tk.END)
        words = content.split()
        word_count = len(words)
        messagebox.showinfo("Word Count", f"Total words: {word_count}")

    def exit_editor(self):
        self.destroy()

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()
