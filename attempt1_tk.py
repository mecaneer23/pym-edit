#!/usr/bin/env python3

from tkinter import ttk, Tk, scrolledtext, Grid, Menu, messagebox, filedialog, END
import os, sys

root = Tk()
root.title("PYM-Edit")
menubar = Menu(root)
root.config(menu=menubar)


def file_new(saved=False):
    if not saved:
        if messagebox.askyesno("Save", "Do you want to save the file?"):
            file_save()
    textbox.delete("1.0", END)


def file_open(file_path):
    if file_path is None:
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select file",
            filetypes=[("All files", "*.*")],
        )
    with open(file_path, "r") as f:
        file = f.read()
    textbox.insert(1.0, file)


def file_save(save_location=None):
    if save_location is None:
        save_location = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Save file as",
            filetypes=[("All files", "*.*")],
        )
    with open(save_location, "w") as f:
        f.write(textbox.get("1.0", END))


menu_file = Menu(menubar, tearoff=0)
menu_file.add_command(label="New", command=file_new)
menu_file.add_command(label="Open", command=file_open)
menu_file.add_command(label="Save", command=file_save)
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

textbox = scrolledtext.ScrolledText(root)
textbox.grid(row=1, column=0, columnspan=4)

root.config(menu=menubar)

if len(sys.argv) > 1:
    file_open(sys.argv[1])
root.mainloop()
