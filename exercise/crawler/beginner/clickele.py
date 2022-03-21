import pyautogui
import os

x=pyautogui.size()
i=pyautogui.position()
print(i,x)
a=0
while True:
    for i in range(1):
        # pyautogui.doubleClick(810,511,duration=-5)
        pyautogui.click(810,511,button='left', clicks=2)
    # pyautogui.doubleClick(949,718,duration=-5)
    # pyautogui.doubleClick(949,718,duration=-5)
    # pyautogui.doubleClick(979,77,duration=-5)

#升級
# while True:
#     pyautogui.doubleClick(949,718,duration=-5)
    