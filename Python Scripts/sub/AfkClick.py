import pyautogui as pga
import time
import sys 
import keyboard

def click_loop():
    #left clicks at a certain point on the screen
    pga.leftClick(940, 520)
    time.sleep(1)



while True:
    click_loop()
    if keyboard.is_pressed("m"):
        sys.exit(0)





    
        
            
        
        
        



