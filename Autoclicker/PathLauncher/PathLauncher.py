import tkinter as tk

import subprocess as cmd
import json as json
import numpy as np
import ast

programs = []
data = np.array([])



current_row = 1

def add_new():
    global current_row
    if current_row > 12:
        return
    k = type(NewButton(current_row))
    current_row += 1


def open_program_on_path(path):
    if path != "":
        cmd.Popen(path)
        #cmd.Popen(path)
    else:
        print("nothing to open!")


def load_data():#loads the json file
    global current_row
    with open(file='C:/Users/User/AppData/Local/savedpaths.json') as f:
        if not f:
            return
        data =ast.literal_eval(json.load(f))
        print(data)

    for i in data:
        k = type(NewButton(current_row))
        k.set_path(k.entry, i)
        print(i)
        current_row += 1


def save_data():##save data within json
    for size in NewButton.path:
        if size.get() != "":
            print(size.get())
            programs.append(size.get())
    data = programs
    with open('C:/Users/User/AppData/Local/savedpaths.json','w') as f:
        json.dump(f'{data}', f)

def clear_paths():
    for children in win.winfo_children():
        children.destroy()

win = tk.Tk()
win.wm_title = "DevKkit Shortcut"
win.geometry("300x500")
win.rowconfigure(1,minsize=20,pad=2,weight=1)
win.maxsize(width=400,height=500)
win.grid_anchor("nw")

button = tk.Button(master=win, text="Add shortcut", command=add_new)
button.grid(column=0,row=0,sticky="nsew")

button_save = tk.Button(text="save", command=save_data)
button_save.grid(column=0,row=1)

button_clear = tk.Button(text="Clear", command=clear_paths)
button_clear.grid(column=1,row=0, sticky="nsew")

lbl_text = tk.Label(text="Add a path to the program to make a shortcut!")

class NewButton:
    path = []
    entry = []
    def __init__(self, row) -> None:
        self.ent = tk.Entry(master=win)
        self.btn = tk.Button(master=win,text="Launch", command=lambda: open_program_on_path(self.ent.get()))
        self.btn.grid(column=1,row=row,sticky="ew")
        self.ent.grid(column=2,row=row,sticky="ew",ipadx=20)
        win.rowconfigure(row,minsize=20,pad=8,weight=10)
        self.entry = self.ent
        NewButton.path.append(self.entry)
        print(self.path)
        NewButton.entry = self.ent
    
    def set_path(self, path):
        self.insert(current_row, path)
        


load_data()
win.mainloop()
