import tkinter as tk

def on_click(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            result = "Invalid Operation"
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid Input")

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Create input fields
label_num1 = tk.Label(app, text="Enter the first number:")
label_num1.pack()
entry_num1 = tk.Entry(app)
entry_num1.pack()

label_num2 = tk.Label(app, text="Enter the second number:")
label_num2.pack()
entry_num2 = tk.Entry(app)
entry_num2.pack()

# Create buttons for arithmetic operations
add_button = tk.Button(app, text="Add (+)", command=lambda: on_click('+'))
add_button.pack()

subtract_button = tk.Button(app, text="Subtract (-)", command=lambda: on_click('-'))
subtract_button.pack()

multiply_button = tk.Button(app, text="Multiply (*)", command=lambda: on_click('*'))
multiply_button.pack()

divide_button = tk.Button(app, text="Divide (/)", command=lambda: on_click('/'))
divide_button.pack()

# Create a label to display the result
label_result = tk.Label(app, text="")
label_result.pack()

# Start the application event loop
app.mainloop()
