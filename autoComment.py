import pyautogui
from time import sleep
from random import randint

x = 500

while True:      
    pyautogui.typewrite(f"Attack By python")
    sleep(.600)                     
    pyautogui.typewrite("\n")          
    sleep(1)                       

    x = x - 1         

    if x == 0:       
        breakU
