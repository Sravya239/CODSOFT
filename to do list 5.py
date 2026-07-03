import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x600")
root.configure(bg="#F0F8FF")
root.resizable(False, False)

tasks = []

title = tk.Label(
    root,
    text="TO-DO LIST APPLICATION",
    font=("Arial", 18, "bold"),
    bg="#F0F8FF",
    fg="navy"
)
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

task_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
task_frame.pack(fill="both", expand=True, padx=20, pady=15)


def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    var = tk.BooleanVar()

    checkbox = tk.Checkbutton(
        task_frame,
        text=task,
        variable=var,
        font=("Arial", 12),
        bg="white",
        anchor="w"
    )

    checkbox.pack(fill="x", padx=10, pady=3)

    tasks.append({
        "task": task,
        "var": var,
        "checkbox": checkbox
    })

    entry.delete(0, tk.END)


def update_task():
    new_task = entry.get().strip()

    if new_task == "":
        messagebox.showwarning("Warning", "Enter updated task.")
        return

    for item in tasks:
        if item["var"].get():
            item["checkbox"].config(text=new_task)
            item["task"] = new_task
            item["var"].set(False)
            entry.delete(0, tk.END)
            return

    messagebox.showinfo("Update", "Select a task using the checkbox.")


def delete_task():
    for item in tasks[:]:
        if item["var"].get():
            item["checkbox"].destroy()
            tasks.remove(item)


def clear_tasks():
    for item in tasks:
        item["checkbox"].destroy()

    tasks.clear()


def show_tasks():
    if len(tasks) == 0:
        messagebox.showinfo("Tasks", "No tasks available.")
        return

    text = ""

    for i, item in enumerate(tasks, start=1):
        status = "Completed" if item["var"].get() else "Pending"
        text += f"{i}. {item['task']} - {status}\n"

    messagebox.showinfo("Task List", text)


button_frame = tk.Frame(root, bg="#F0F8FF")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add",
    width=12,
    bg="lightgreen",
    command=add_task
).grid(row=0, column=0, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Update",
    width=12,
    bg="lightblue",
    command=update_task
).grid(row=0, column=1, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Delete",
    width=12,
    bg="tomato",
    command=delete_task
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Show Tasks",
    width=12,
    bg="khaki",
    command=show_tasks
).grid(row=1, column=1, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Clear All",
    width=12,
    bg="orange",
    command=clear_tasks
).grid(row=2, column=0, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Exit",
    width=12,
    bg="lightgray",
    command=root.destroy
).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()