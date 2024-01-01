import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

screen = tk.Tk()
screen.title("To-Do List")

task_listbox = tk.Listbox(screen, height=15, width=40)
task_listbox.pack(pady=10)

task_entry = tk.Entry(screen, width=40)
task_entry.pack()

add_button = tk.Button(screen, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(screen, text="Delete Task", command=remove_task)
remove_button.pack()

update_button = tk.Button(screen, text="Update Task", command=update_task)
update_button.pack()

screen.mainloop()