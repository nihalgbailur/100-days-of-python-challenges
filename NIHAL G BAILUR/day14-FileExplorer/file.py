import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content_text.delete(1.0, tk.END)
            content_text.insert(tk.END, file.read())

app = tk.Tk()
app.title("File Explorer")

open_button = tk.Button(app, text="Open File", command=open_file)
open_button.pack()

content_text = tk.Text(app)
content_text.pack()

app.mainloop()
