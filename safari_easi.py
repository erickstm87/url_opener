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
bashCommand = "sudo killall 'Safari' "
#bashCommand = "sudo killall -r 'google'"
new = 1
file1 = open('incon.txt', 'r')
x = 0
def incontent_noauto():
    j = 0
    b.open(i,new=new)
    for j in range(0,16):
        pyautogui.press('down')
    time.sleep(2)
    pyautogui.click(444,551)
    time.sleep(2)
    pyautogui.click(264,687)
    time.sleep(2)
    os.system(bashCommand)

def incontent_auto():
    j = 0 
    b.open(i,new=new)
    for j in range(0,16):
        pyautogui.press('down')
    #ad interactivity still to come
    
for i in file1:
    if 'incontent' and 'spotx_autoplay=0' in i:
        incontent_noauto()
    elif 'incontent' and 'spotx_autoplay=&' in i:
        incontent_auto()
    #webbrowser.open(i,new=new)
    

    
    

