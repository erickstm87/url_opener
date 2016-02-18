#!/usr/bin/env python
import webbrowser
import csv
import numpy as np
import sys
import os
import time
import pyautogui
from subprocess import call
#for installation of pyautogui on mac check out http://stackoverflow.com/questions/35051580/phyton3-pip-and-pyautogui-install-mac-remove-broken-python and go to the bottom 

pyautogui.size()
width,height = pyautogui.size()
b = webbrowser.get('safari')
#bashCommand = "/bin/bash kill.sh"
bashCommand = "sudo killall 'Safari' "
#bashCommand = "sudo killall -r 'google'"
new = 1
file1 = open('int_test.txt', 'r')
x = 0
for i in file1:
    x += 1
    b.open(i,new=new)
    #webbrowser.open(i,new=new)
    time.sleep(3)
    pyautogui.click(548,438)
    time.sleep(2)
    call(["screencapture", "screenshot_play(%s).jpg" % x]) 
    time.sleep(2)
    pyautogui.click(809,808)
    time.sleep(4)
    call(["screencapture", "screenshot_full(%s).jpg" % x])
    pyautogui.click(1430,890)
    time.sleep(2)
    call(["screencapture", "screenshot_full_exit(%s).jpg" % x])
    pyautogui.click(270,807)
    call(["screencapture", "screenshot_pause(%s).jpg" % x])
    time.sleep(3)
    pyautogui.click(270,807)
    call(["screencapture", "screenshot_replay(%s).jpg" % x])
    time.sleep(10)
    os.system(bashCommand)
    '''if x==1:
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
        os.system(bashCommand)'''
    
    
    

