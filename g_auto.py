
import pyautogui

pyautogui.size()
width,height = pyautogui.size()
for i in range(10):
    pyautogui.moveTo(100,100,duration=.25)
    pyautogui.moveTo(100,200,duration=.25)
    pyautogui.moveTo(200,200,duration=.25)
    pyautogui.moveTo(100,200,duration=.25)
