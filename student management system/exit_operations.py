# exit_operations.py

from tkinter import messagebox

def handle_exit(root):
    result = messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit?')
    if result:
        root.destroy()
    else:
        pass
