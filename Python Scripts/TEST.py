import time
import customtkinter as ctk
import threading as th
import keyboard
import sys

#mainwindow
mainwindow = ctk.CTk()
mainwindow.geometry("300x250")
mainwindow.title("Quick Click")

#adding a frame to put things inside of(frame is in the mainwindow)w
frame = ctk.CTkFrame(master=mainwindow)
frame.pack(pady = 12, padx = 10)

switch_var1 = ctk.StringVar(value="off")
switch_var2 = ctk.StringVar(value="off")

#two butttons that display text and run the above methods/functions
buttonclick = ctk.CTkSwitch(master=frame, text="Afk Clicker", variable=switch_var1, onvalue="on", offvalue="off")
buttonclick.pack(padx=10, pady=10)


buttonmine = ctk.CTkSwitch(master=frame, text="Afk Miner", onvalue="on", offvalue="off")
buttonmine.pack(padx=10, pady=10)

#used to check the state of a switch
var1 = buttonclick.get()
if var1 == "off":
    print("TEST")
if keyboard.is_pressed("m"):
    sys.exit(0)

#listens for events and does them, like an ending to a loop or something like that
mainwindow.mainloop()

