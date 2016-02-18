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
new = 1
file1 = open('tester.txt', 'r')
x = 0
for i in file1:
    x += 1
    b.open(i,new=new)
    #webbrowser.open(i,new=new)
    time.sleep(5)
    '''pyautogui.click(271,811)
    time.sleep(3)
    os.system(bashCommand)'''
    if x==1:
        pyautogui.click(530,44)
        time.sleep(3)
        os.system(bashCommand)
    elif x==2:
        pyautogui.click(1015,90,duration=.9)
        time.sleep(3)
        os.system(bashCommand)
    else:
        pyautogui.click(454,264,duration=.9)
        time.sleep(3)
        os.system(bashCommand)
    
    
    

