import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def complete_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        tasks_listbox.itemconfig(selected_index, {'foreground': 'gray'})
        tasks_listbox.selection_clear(0, tk.END)

def delete_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        tasks_listbox.delete(selected_index)

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create an entry for new tasks
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Create buttons to add, complete, and delete tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

complete_button = tk.Button(app, text="Complete Task", command=complete_task)
complete_button.pack()

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack()

# Create a listbox to display the tasks
tasks_listbox = tk.Listbox(app, selectbackground="#a6a6a6")
tasks_listbox.pack(pady=10)

# Start the application event loop
app.mainloop()
