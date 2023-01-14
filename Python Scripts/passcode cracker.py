# imports
import random
import keyboard
import pyautogui as pga
import string
import time

used_pass = []


def user_input():
    global length
    length = int(input("Enter length of password(1-10) "))


user_input()


# hotkeys that will use the variables above
def hotkeys():


    # moves mouse to center of screen and clicks
    pga.moveTo(960, 540)
    pga.leftClick()

    global temp

    time.sleep(3)
    while True:



        # randomizing of the digits
        digits = string.digits
        try:
            temp = random.sample(str(digits), length)
            password = "".join(temp)
            used_pass.append(password)

            if password in used_pass:
                print(f'detected {used_pass}')
                temp = random.sample(str(digits), length)
                password = "".join(temp)



            # typing of password

            pga.typewrite(f'{password}')
            pga.hotkey("enter")
            pga.hotkey("enter")

            # stops program

            if keyboard.is_pressed("w"):
                break

        except ValueError:
            print("length over 10!")
            user_input()


hotkeys()
