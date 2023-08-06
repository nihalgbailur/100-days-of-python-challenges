import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters
    if include_digits_var.get():
        characters += string.digits
    if include_special_chars_var.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_result.config(text=f"Generated Password: {password}")

# Create the main application window
app = tk.Tk()
app.title("Random Password Generator")

# Create a label and entry for password length
length_label = tk.Label(app, text="Enter Password Length:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

# Create checkboxes for options
include_digits_var = tk.BooleanVar()
include_digits_var.set(True)
include_digits_checkbox = tk.Checkbutton(app, text="Include Digits (0-9)", variable=include_digits_var)
include_digits_checkbox.pack()

include_special_chars_var = tk.BooleanVar()
include_special_chars_var.set(True)
include_special_chars_checkbox = tk.Checkbutton(app, text="Include Special Characters", variable=include_special_chars_var)
include_special_chars_checkbox.pack()

# Create a button to generate the password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label to display the generated password
password_result = tk.Label(app, text="", wraplength=300)
password_result.pack(pady=20)

# Start the application event loop
app.mainloop()
