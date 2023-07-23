import os , sys , time, shutil
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
import threading as thread

import tkinter as tk

is_active = False

cps = 1.0

button_type = Button.left

def auto_click():#main fuction of the program
    global is_active, cps, button_type
    mouse = Controller()
    while is_active:
        mouse.click(button_type, 1)
        time.sleep(cps)


def on_pressed(key):
    global is_active
    if key == Key.f7:
        if not is_active:
            print("auto click activated")
            is_active = True
            lbl_activate["text"] = "Activated"
            
            start_click_on_thread()
            
        else:
            is_active = False
            print("decativated")
            lbl_activate["text"] = "Deactivated"

def start_click_on_thread():
    auto_click_thread = thread.Thread(target=auto_click)
    auto_click_thread.daemon = True
    auto_click_thread.start()


def cps_apply():#apply time
    global cps
    cps = float(ent_cps.get())

def start_listening():#start listening to key events
    with Listener(on_release=on_pressed) as listener:
        listener.join()

def update():#updates per provided ms
    global cps
    window.wm_title(f"AMUI module - t:{cps}, btn:{button_type}")
    window.after(200, update)
    if ent_cps.get() == "":
        return
    cps = float(ent_cps.get())

def switch_input(event):
    global button_type
    selected_value = var.get()
    if selected_value == "Left":
        button_type = Button.left
    elif selected_value == "Right":
        button_type = Button.right
    else:
        button_type = Button.middle
    print(f"type:{selected_value}")


icon_name = "mouse.ico"

listener_thread = thread.Thread(target=start_listening)
listener_thread.daemon = True
listener_thread.start()


##############IMAGE############################################
def get_icon_path(filename):
    base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(base_path, filename)

window = tk.Tk()
icon_path = get_icon_path(icon_name)

if os.path.exists(icon_path):
    window.iconbitmap(icon_path)
else:
    print("icon file not found!",icon_path)
##############################################################
window.minsize(350,300)
window.maxsize(350,300)
window.wm_title("AMUI module")
window.configure(background="gray10")

frame_grid = tk.Frame(master=window, bg="gray20")
frame_grid.grid(columnspan=2,rowspan=2,row=0,column=0,
                padx=30,pady=10)

lbl_activate = tk.Label(master=frame_grid,text="Deactivated",
                        bg="gray20",fg="white")
lbl_activate.grid(columnspan=2,column=1,row=1)
lbl_cps = tk.Label(master=frame_grid,text="Time per clicks : ",
                   bg="gray20",fg="white")
lbl_cps.grid(column=0,row=2)
ent_cps = tk.Entry(master=frame_grid,bg="gray10",fg="white",
                   width=20,borderwidth=10,border=1,insertbackground="white")
ent_cps.grid(column=1,row=2)

btn_apply = tk.Button(master=frame_grid,relief="flat",text="Apply",command=cps_apply,
                      bg="gray20",fg="white")
btn_apply.grid(column=2,row=2)

options = ["Left","Right","Middle"]

var = tk.StringVar(window)
var.set(options[0])

lbl_option = tk.Label(master=frame_grid,text="Simulate Input Key: ",
                      bg="gray20",fg="white")
lbl_option.grid(column=0,row=3)
Option_btn = tk.OptionMenu(frame_grid, var,*options,command=switch_input)
Option_btn.grid(column=1,row=3)

update()

window.mainloop()


