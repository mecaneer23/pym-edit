#!/usr/bin/env python3

from tkinter import ttk, Tk, scrolledtext, Grid, Menu, messagebox, filedialog

root = Tk()
root.title("PYM-Edit")

menubar = Menu(root)

menu_file = Menu(menubar, tearoff=0)
menu_file.add_command(label="New", command=lambda: None)
menu_file.add_command(label="Open", command=lambda: None)
menu_file.add_command(label="Save", command=lambda: None)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.destroy)

# menu_edit = Menu(menubar, tearoff=0)
# menu_edit.add_command(label="Undo -- Ctrl + Z", command=lambda: None)
# menu_edit.add_command(label="Redo -- Ctrl + Shift + Z", command=lambda: None)
# menu_edit.add_separator()
# menu_edit.add_command(label="Cut -- Ctrl + X", command=lambda: None)
# menu_edit.add_command(label="Copy -- Ctrl + C", command=lambda: None)
# menu_edit.add_command(label="Paste -- Ctrl + V", command=lambda: None)

menu_help = Menu(menubar, tearoff=0)
menu_help.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        title="About", message="PYM-Edit\n\nVersion 1.0"
    ),
)

menubar.add_cascade(label="File", menu=menu_file)
# menubar.add_cascade(label="Edit", menu=menu_edit)
menubar.add_cascade(label="Help", menu=menu_help)

scrolledtext.ScrolledText(root).grid(row=1, column=0, columnspan=4)

root.config(menu=menubar)
root.mainloop()
