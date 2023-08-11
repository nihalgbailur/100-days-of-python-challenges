import tkinter as tk
from tkinter import messagebox

def save_note():
    note = note_text.get("1.0", tk.END)
    if note.strip():
        with open('notes.txt', 'a') as file:
            file.write(note + '\n')
        messagebox.showinfo("Note Saved", "Note has been saved successfully.")

def view_notes():
    try:
        with open('notes.txt', 'r') as file:
            notes = file.read()
        note_text.delete("1.0", tk.END)
        note_text.insert(tk.END, notes)
    except FileNotFoundError:
        messagebox.showinfo("No Notes", "No notes found.")

# Create the main application window
app = tk.Tk()
app.title("Note-taking App")

# Create a text widget for note input
note_text = tk.Text(app, height=10, width=40)
note_text.pack(pady=10)

# Create buttons to save and view notes
save_button = tk.Button(app, text="Save Note", command=save_note)
save_button.pack()

view_button = tk.Button(app, text="View Notes", command=view_notes)
view_button.pack()

# Start the application event loop
app.mainloop()
