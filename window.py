# GUI of Root Window

import socket
import threading
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import time

key = 8061
all_data = ''
server = ("192.168.1.101", 9090)                 # Input there your Server ip address

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.1.101', 0))
s.setblocking(0)

def window(username):

    def clicked():
        if input_text.get() != '':
            message = input_text.get()
            crypt = ""
            for i in message:
                crypt += chr(ord(i)^key)
            s.sendto(("[" + username + "] :: " + crypt).encode("utf-8"), server)
            time.sleep(0.2)
            label.config(state = "normal")
            temp = label.get(1.0, END)
            if temp[0] == '\n':
                temp = temp[1:]
            message = '[you] :: ' + message
            message = temp + message
            label.delete(1.0, END)
            label.insert(1.0, message)
            label.config(state = "disabled")
            input_text.delete(0, END)


    root = Tk()
    root['bg'] = '#303F9F'
    root.title('Messenger')
    root.wm_attributes('-alpha', 0.7)
    root.geometry('750x500')
    root.resizable(width = False, height = False)

    def on_closing():
        s.sendto(("[" + username + "] <= left chat ").encode("utf-8"), server)
        root.destroy()
        s.close()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    #---------------Text-------------------------
    mainFrame = Frame(root)
    mainFrame.grid()

    entryFrame = Frame(mainFrame, width=700, height=400, background = '#303F9F')
    entryFrame.grid(row=0, column=1)
    entryFrame.columnconfigure(0, weight=40)
    entryFrame.grid_propagate(False)

    label = scrolledtext.ScrolledText(entryFrame, font=("Arial Bold", 10))
    label.grid(column=0, row=0, pady = 20)
    label.insert(INSERT, all_data)
    label.config(state = "disabled")
    #--------------------------------------------

    #------------Input Text----------------------
    input_text = Entry(root, width = 72, font = 7)
    input_text.grid(column=0, row=2, pady = 10, padx = 10)
    input_text.focus()
    #--------------------------------------------

    #-------------Button-------------------------
    btn = Button(root, text="Send Message", command = clicked, height = 1, width = 60, background = '#9E9E9E', activebackground = '#757575', foreground = '#FFFFFF')
    btn.grid(column=0, row=3, pady = 10, padx = 30)
    #--------------------------------------------


    def receving (name, sock):
        while True:
            try:
                while True:
                    data, addr = sock.recvfrom(1024)

                    decrypt = ""; k = False
                    for i in data.decode("utf-8"):
                        if i == ":":
                            k = True
                            decrypt += i
                        elif k == False or i == " ":
                            decrypt += i
                        else:
                            decrypt += chr(ord(i)^key)
                    all_data = label.get(1.0, END) + decrypt
                    if all_data[0] == '\n':
                        all_data = all_data[1:]
                    #print(all_data)

                    label.config(state = "normal")
                    label.delete(1.0, END)
                    label.insert(1.0, all_data, END)
                    label.config(state = "disabled")

                    time.sleep(0.2)
            except:
                pass

    s.sendto(("[" + username + "] => join chat ").encode("utf-8"), server)

    rT = threading.Thread(target = receving, args = ("RecvThread", s), daemon=True)
    rT.start()

    root.mainloop()
