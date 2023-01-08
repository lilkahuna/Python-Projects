import pydirectinput as pdi
import time, keyboard
import sys


#time before program start
time.sleep(3)

def mine():
    pdi.mouseDown()
    time.sleep(2)
    pdi.mouseUp()


def walk():
    pdi.keyDown("w")
    time.sleep(2)
    pdi.keyUp("w")
    

def dig():
    mine()
    time.sleep(0.5)
    walk()


while True:
    dig()
    if keyboard.is_pressed("m"):
        sys.exit(0)
