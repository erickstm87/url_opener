#!/usr/bin/env python
import webbrowser
import csv
import numpy as np
import sys
import os
import time
import pyautogui
#for installation of pyautogui on mac check out http://stackoverflow.com/questions/35051580/phyton3-pip-and-pyautogui-install-mac-remove-broken-python and go to the bottom 

pyautogui.size()
width,height = pyautogui.size()
b = webbrowser.get('safari')
#bashCommand = "/bin/bash kill.sh"
bashCommand = "sudo killall 'Safari' "
#bashCommand = "sudo killall -r 'google'"
new = 2
new_file = []
file1 = open('text.txt')
for row in file1:
    new_file.append(row)
x = 0
for i in new_file:
    x += 1
    b.open(i,new=new)
    #webbrowser.open(i,new=new)
    time.sleep(5)
    if x==1:
        pyautogui.click(386,335)
        time.sleep(3)
        os.system(bashCommand)
    elif x==2:
        pyautogui.click(378,335,duration=.9)
        time.sleep(3)
        os.system(bashCommand)
    else:
        pyautogui.click(400,200,duration=.9)
        time.sleep(3)
        os.system(bashCommand)
    
    
    

