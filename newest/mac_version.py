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
    time.sleep(3) #wait for the ad to load
    pyautogui.click(548,438) #click to play and start the ad
    time.sleep(2)
    call(["screencapture", "screenshot_play(%s).jpg" % x]) #screenshot of ad started
    time.sleep(2)
    pyautogui.click(673,470) #click to clickthrough the ad to their page
    time.sleep(3) #wait for webpage to load
    call(["screencapture", "screenshot_clickthrough(%s).jpg" % x]) #make sure webpage pulled up
    pyautogui.click(741,76) #exit out of webpage
    time.sleep(3) #get back to the ad
    pyautogui.moveTo(270,807) #move to the position where the play icon is
    pyautogui.click(270,807) #resume the ad after returning from webpage
    time.sleep(3) 
    pyautogui.click(809,808) #this sends the ad into full screen
    time.sleep(4)
    call(["screencapture", "screenshot_full(%s).jpg" % x]) #take a screenshot of ad in full screen
    pyautogui.click(1430,890) #exit out of full screen
    time.sleep(2)
    call(["screencapture", "screenshot_full_exit(%s).jpg" % x]) #probably unnecessary captures the ad after it's returned
    pyautogui.click(270,807) #pause the ad
    call(["screencapture", "screenshot_pause(%s).jpg" % x])
    time.sleep(3)
    pyautogui.click(270,807) #resume
    time.sleep(1)
    call(["screencapture", "screenshot_replay(%s).jpg" % x])
    time.sleep(7) #let the ad finish could be calibrated
    os.system(bashCommand) #kill the browser
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
    
    
    

