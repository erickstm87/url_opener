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
file1 = open('another.txt', 'r')
#file1 = raw_input('whats the filename of your urls? make sure its a txt file, you dont need to type in the file extension \n') + '.csv'
x = 0

def incontent_noauto():
    j = 0
    b.open(i,new=new)
    time.sleep(20)
    for j in range(0,37):
        pyautogui.press('down')
    pyautogui.press('s')#starts the ad
    time.sleep(2)
    #pyautogui.click('')#write this out to clickthrough
    #pyautogui.keydown('command')#closes out the tab
    #pyautogui.keypress('w')
    #pyautogui.keyup('command')
    time.sleep(2)
    #pyautogui.moveTo(630,668)#this is to go full screen
    time.sleep(1)
    #pyautogui.press('esc')
    time.sleep(2)
    pyautogui.press('p')#pause the ad
    time.sleep(1)
    pyautogui.press('r')#resume the ad
    for j in range(0,38):
        pyautogui.press('up')
    os.system(bashCommand)
'''
def incontent_auto():
    j = 0 
    b.open(i,new=new)
    for j in range(0,16):
        pyautogui.press('down')
    #ad interactivity still to come
'''
def instream_noauto():
    time.sleep(15)
    pyautogui.press('s')#starts the ad
    time.sleep(2)
    pyautogui.click('')#write this out to clickthrough
    '''pyautogui.keydown('command')#closes out the tab
    pyautogui.keypress('w')
    pyautogui.keyup('command')'''
    time.sleep(2)
    #pyautogui.moveTo(630,668)#this is to go full screen
    #time.sleep(1)
    #pyautogui.press('esc')
    time.sleep(2)
    pyautogui.press('p')#pause the ad
    time.sleep(1)
    pyautogui.press('r')#resume the ad
    os.system(bashCommand)

def instream_auto():
    time.sleep(15)
    '''pyautogui.click('')#write this out to clickthrough
    pyautogui.keydown('command')#closes out the tab
    pyautogui.keypress('w')
    pyautogui.keyup('command')'''
    time.sleep(2)
    #pyautogui.moveTo(630,668)#this is to go full screen
    time.sleep(1)
    #pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('p')#pause the ad
    time.sleep(1)
    pyautogui.press('r')#resume the ad
    time.sleep(10)
    os.system(bashCommand)

def main():
    for i in file1:
        if 'incontent' and 'spotx_autoplay=0' in i:
            incontent_noauto()
        elif 'instream' and 'spotx_autoplay=0' in i:
            instream_noauto()
        elif 'instrem' and 'spotx_autoplay=&' in i:
            instream_auto()
        '''elif 'incontent' and 'spotx_autoplay=&' in i:
        incontent_auto()'''
        #webbrowser.open(i,new=new)
        except KeyboardInterrupt:
            print '\nPausing... (Hit ENTER to continue, type quit to exit, or c to copy the url to the failed file.)'
            try:
                response = raw_input()
                if response == 'quit':
                    exit()
                elif response == 'c':

                except KeyboardInterrupt:
                    print 'Resuming...'
                    continue
main()
    

    
    

