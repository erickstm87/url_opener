import pyautogui
import webbrowser

x,y = pyautogui.locateCenterOnScreen('player.png',grayscale=True)
j,s = (int(x/2),int(y/2))
print(j,s)