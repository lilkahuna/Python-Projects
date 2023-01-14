import customtkinter as ctk


# this is a demo for using th enter key to call a function then delete text inside an entry

# *args is a wild card argument meaning anything can be sent to this function
def do_stuff(event):
    value = text.get()
    if value == "DOG":
        print("HEORRAY")
    # deletes from the 0 element(first letter or number) then to the end of the text entered
    text.delete(0, 'end')


mainwindow = ctk.CTk()

text = ctk.CTkEntry(master=mainwindow, placeholder_text="Type here")
text.bind("<Return>", do_stuff)
text.pack(padx=10, pady=10)

mainwindow.mainloop()
