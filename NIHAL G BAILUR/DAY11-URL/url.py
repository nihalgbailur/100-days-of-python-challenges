import tkinter as tk
from pyshorteners import Shortener
import tkinter.messagebox

def shorten_url():
    long_url = long_url_entry.get()
    if long_url:
        s = Shortener()
        short_url = s.tinyurl.short(long_url)
        short_url_label.config(text=f"Shortened URL: {short_url}")
        copy_button.config(state=tk.NORMAL)
    else:
        short_url_label.config(text="Enter a valid URL")
        copy_button.config(state=tk.DISABLED)

def copy_to_clipboard():
    short_url = short_url_label.cget("text")
    short_url = short_url.replace("Shortened URL: ", "")
    root.clipboard_clear()
    root.clipboard_append(short_url)
    root.update()
    tkinter.messagebox.showinfo("Copied", "Shortened URL copied to clipboard!")

# Create the main application window
root = tk.Tk()
root.title("URL Shortener")

# Create an entry for long URL input
long_url_entry = tk.Entry(root)
long_url_entry.pack(pady=10)

# Create a button to shorten the URL
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack()

# Create a label to display the shortened URL
short_url_label = tk.Label(root, text="", font=("Helvetica", 12))
short_url_label.pack(pady=20)

# Create a button to copy the shortened URL
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack()

# Start the application event loop
root.mainloop()
