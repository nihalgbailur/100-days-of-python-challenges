import tkinter as tk
from collections import Counter
import re
from tkinter import filedialog

def analyze_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    with open(file_path, 'r') as file:
        input_text = file.read()

    words = re.findall(r'\w+', input_text.lower())
    
    total_word_count = len(words)
    word_freq = Counter(words)
    most_common_word = word_freq.most_common(1)
    
    result_text = f"Total Word Count: {total_word_count}\n\n"
    result_text += "Word Frequency:\n"
    
    for word, freq in word_freq.items():
        result_text += f"{word}: {freq}\n"
    
    result_text += f"\nMost Common Word: {most_common_word[0][0]}"
    result_widget.config(state=tk.NORMAL)
    result_widget.delete("1.0", tk.END)
    result_widget.insert(tk.END, result_text)
    result_widget.config(state=tk.DISABLED)

# Create the main application window
app = tk.Tk()
app.title("Text Analyzer")

# Create a button to analyze text from a file
analyze_button = tk.Button(app, text="Analyze Text from File", command=analyze_text)
analyze_button.pack()

# Create a text widget to display the analysis result
result_widget = tk.Text(app, height=10, width=40, state=tk.DISABLED)
result_widget.pack()

# Start the application event loop
app.mainloop()
