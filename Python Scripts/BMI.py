import customtkinter as ctk


# variables
# none assigns no value to a variable just like saying public string emptyString; in java


# Functions for bmi
def do_bmi():
    try:

        weightvar = float(weight.get())
        heightvar = float(height.get())
        # bmi calculation
        bmi = (weightvar * 703) / (heightvar * heightvar)

        # tells if you are over under or good weight
        if bmi >= 25:
            weightstring = " you are overweight"
        elif bmi < 25 and bmi > 18.5:
            weightstring = " you are a healthy weight"
        elif bmi < 18.5:
            weightstring = " you are underweight"
        else:
            print("ERROR")

        sum = ctk.CTkToplevel()
        sum.geometry("500x100")
        sum.title("Your BMI (close when done)")

        # format used to add the bmi variable to a label because the label is a string and the bmi is an int
        # could use f string too
        label = ctk.CTkLabel(master=sum, text=f'your bmi is: {bmi} , {weightstring}')
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    except ValueError:
        # creating error box
        errors = ctk.CTkToplevel()
        errors.geometry("500x100")
        errors.title("Error! (close when done)")

        # display error label
        labelerror = ctk.CTkLabel(master=errors, text="Invalid input, please try again")
        labelerror.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    except ZeroDivisionError:
        # creating error box
        errors = ctk.CTkToplevel()
        errors.geometry("500x100")
        errors.title("Error! (close when done)")

        # display error label
        labelerror = ctk.CTkLabel(master=errors, text="Can't divide by zero try again")
        labelerror.pack(side="top", fill="both", expand=True, padx=40, pady=40)


# gui main window
mainwindow = ctk.CTk()
mainwindow.geometry("300x400")
mainwindow.title("BMI Calculator")

frame = ctk.CTkFrame(master=mainwindow)
frame.pack()

weightlab = ctk.CTkLabel(master=frame, text="Weight: ")

weightlab.pack(padx=10, pady=10)
weight = ctk.CTkEntry(master=frame, placeholder_text="Enter weight in pounds")
weight.pack()

heightlab = ctk.CTkLabel(master=frame, text="Height: ")

heightlab.pack()
height = ctk.CTkEntry(master=frame, placeholder_text="Enter height in inches")
height.pack(padx=10, pady=10)

submit = ctk.CTkButton(master=frame, text="Submit", fg_color="#4eef8f", text_color="#242825", command=do_bmi,
                       hover_color="#0fab4e")
submit.pack(padx=10, pady=10)

mainwindow.mainloop()
