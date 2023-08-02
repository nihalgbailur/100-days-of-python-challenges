import tkinter as tk
import random 

# List of quotes
quotes = [
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Don't cry because it's over, smile because it happened. - Dr. Seuss",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost"
]

def get_random_quote():
    return random.choice(quotes)

# Create the main application window
app = tk.Tk()
app.title("Random Quote Generator")

# Create a label to display the quote
quote_label = tk.Label(app, text="", wraplength=300)
quote_label.pack(pady=20)

def generate_quote():
    random_quote = get_random_quote()
    quote_label.config(text=random_quote)

# Create a button to generate a new quote
generate_button = tk.Button(app, text="Generate Quote", command=generate_quote)
generate_button.pack()

# Generate the first quote on application start
generate_quote()

# Start the application event loop
app.mainloop()
