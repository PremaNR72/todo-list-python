import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.title("To-Do List App")
window.geometry("400x400")

tasks = []

# Add task function
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Delete task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
    else:
        messagebox.showwarning("Warning", "Please select a task")

# Mark completed
def mark_completed():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected[0])
        listbox.delete(selected[0])
        listbox.insert(tk.END, task + " ✔")

# Input box
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Buttons
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

complete_button = tk.Button(window, text="Mark Completed", command=mark_completed)
complete_button.pack()

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

# Task list
listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=20)

# Run app
window.mainloop()