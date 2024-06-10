# Hamester Kombat Auto_Clicker

import time
import threading 
from pynput.mouse import Controller,Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="t")

CL = False 
MOUSE = Controller()

def AutoClicking():
    while True:
        if CL:
            MOUSE.click(Button.left, 1)
        time.sleep(0.0001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global CL
        CL = not CL
        
CT = threading.Thread(target=AutoClicking)
CT.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()