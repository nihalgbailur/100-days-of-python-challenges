import tkinter as tk

conversion_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "JPY": 110.77,
    "GBP": 0.72,
    "AUD": 1.34,
    # Add more conversion rates here
}

def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_entry.get())

    converted_amount = amount * (conversion_rates[to_currency] / conversion_rates[from_currency])
    result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")

# Create the main application window
app = tk.Tk()
app.title("Currency Converter")

# Create drop-down menus for currency selection
from_currency_var = tk.StringVar(value="USD")
from_currency_menu = tk.OptionMenu(app, from_currency_var, *conversion_rates.keys())
from_currency_menu.pack(pady=10)

to_currency_var = tk.StringVar(value="EUR")
to_currency_menu = tk.OptionMenu(app, to_currency_var, *conversion_rates.keys())
to_currency_menu.pack(pady=10)

# Create an entry for amount input
amount_entry = tk.Entry(app)
amount_entry.pack(pady=10)

# Create a button to convert currency
convert_button = tk.Button(app, text="Convert", command=convert_currency)
convert_button.pack()

# Create a label to display the converted amount
result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the application event loop
app.mainloop()
