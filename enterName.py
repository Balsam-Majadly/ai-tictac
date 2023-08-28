import tkinter as tk
from tkinter import simpledialog


def get_names():
    name1 = simpledialog.askstring("Name Entry", "Enter Name 1:")
    name2 = simpledialog.askstring("Name Entry", "Enter Name 2:")

    if name1 and name2:
        result_label.config(text=f"Names entered: {name1}, {name2}")
    elif name1:
        result_label.config(text=f"Name 1 entered: {name1}")
    elif name2:
        result_label.config(text=f"Name 2 entered: {name2}")
    else:
        result_label.config(text="No names entered.")


root = tk.Tk()
root.title("Enter Names")

button = tk.Button(root, text="Enter Names", command=get_names)
button.pack()

result_label = tk.Label(root, text="Please enter names.")
result_label.pack()

root.mainloop()