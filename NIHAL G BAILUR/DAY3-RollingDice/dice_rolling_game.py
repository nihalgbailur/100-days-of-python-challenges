import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=f"You rolled a {result}!")

# Create the main application window
app = tk.Tk()
app.title("Dice Rolling Game")

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Helvetica", 20))
result_label.pack(pady=20)

# Create a button to roll the dice
roll_button = tk.Button(app, text="Roll Dice", font=("Helvetica", 16), command=roll_dice)
roll_button.pack()

# Start the application event loop
app.mainloop()
