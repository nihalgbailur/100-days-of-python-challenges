import tkinter as tk
import random

def flip_coin():
    result = random.choice(["Heads", "Tails"])
    result_label.config(text=f"The coin landed on: {result}!")

# Create the main application window
app = tk.Tk()
app.title("Coin Flipping Game")

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Helvetica", 20))
result_label.pack(pady=20)

# Create a button to flip the coin
flip_button = tk.Button(app, text="Flip Coin", font=("Helvetica", 16), command=flip_coin)
flip_button.pack()

# Start the application event loop
app.mainloop()
