import customtkinter as ctk

d = []
f = []


def writetofile():
    store = open("Store.txt", "a")

    userinput = input("Enter something")
    amount = input("Enter amount")
    store.write(f'\n{userinput}, {amount}')


writetofile()


def check_groceries():
    input = searchbar.get()
    store = open("Store.txt", "r")
    for i in store:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    storedata = dict(zip(d, f))

    number = storedata.get(input)

    # number = storedict.get(input)
    if input in storedata:
        displaylab.configure(text=f'{input}, is avalible: {number}')
    else:
        displaylab.configure(text=f'Cant find {input}')


mainwindow = ctk.CTk()
mainwindow.geometry("300x500")
mainwindow.title("Avalibility Tracker")

label = ctk.CTkLabel(master=mainwindow, text="Groceries avalibility", font=("Arial", 25))
label.pack(padx=10, pady=10)

frame = ctk.CTkFrame(master=mainwindow)
frame.pack(padx=10, pady=10)

searchbar = ctk.CTkEntry(master=frame, placeholder_text="search for a food")
searchbar.pack(padx=10, pady=10)

submitbutton = ctk.CTkButton(master=frame, text="submit", command=check_groceries)
submitbutton.pack()

displaylab = ctk.CTkLabel(master=frame, text=" ")
displaylab.pack()
mainwindow.mainloop()
