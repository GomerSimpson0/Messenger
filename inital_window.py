# GUI of Inital Window

import window
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

def inital_window():

    def commit_username():
        alias_name = input_text.get()
        inital_root.destroy()
        window.window(alias_name)

    inital_root = Tk()
    inital_root['bg'] = '#fafafa'
    inital_root.title('Inital Window')
    inital_root.wm_attributes('-alpha', 0.7)
    inital_root.geometry('250x200')
    inital_root.resizable(width = False, height = False)

    #---------------Text-------------------------
    label = Label(inital_root, text="Input Username", font=("Arial Bold", 14))
    label.grid(column=0, row=0, padx = 50, pady = 30)
    #--------------------------------------------

    #------------Input Text----------------------
    input_text = Entry(inital_root, width = 25)
    input_text.grid(column=0, row=2)
    input_text.focus()
    #--------------------------------------------

    #-------------Button-------------------------
    btn = Button(inital_root, text="Join Chat", command = commit_username, height = 1, width = 10)
    btn.grid(column=0, row=3, pady = 20)
    #--------------------------------------------

    inital_root.mainloop()


