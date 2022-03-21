import pyautogui
import time
import os

x=pyautogui.size()
i=pyautogui.position()
print(i,x)

while True:
    pyautogui.moveTo(150,400,duration=5)
    pyautogui.moveTo(850,154,duration=5)
    pyautogui.moveTo(500,1024,duration=5)
    time.sleep(5)