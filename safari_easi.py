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
new = 1
file1 = open('incon.txt', 'r')
#file1 = raw_input('whats the filename of your urls? make sure its a txt file, you dont need to type in the file extension \n') + '.csv'
x = 0

def ad_spotter():
    x,y = pyautogui.locateCenterOnScreen('ad_here.png')
    pyautogui.moveTo(x,(y-10))

def full_screen():
    time.sleep(2)
    x, y = pyautogui.locateCenterOnScreen('full_screen.png')
    pyautogui.click(x,y)
    time.sleep(3)

def scroll_down():
    j = 0
    for j in range(0,37):
        pyautogui.press('down')
    pyautogui.press('s')#starts the ad
    time.sleep(2)

def scroll_up():
    j = 0
    for j in range(0,38):
        pyautogui.press('up')

def close_tab():
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')

def incontent_noauto(i):
    b.open(i,new=new)
    time.sleep(3)
    scroll_down()
    ad_spotter()
    #pyautogui.click('')#write this out to clickthrough
    #pyautogui.keydown('command')#closes out the tab
    #pyautogui.keypress('w')
    #pyautogui.keyup('command')
    full_screen()
    pyautogui.press('esc')
    time.sleep(2)
    pyautogui.press('p')#pause the ad
    time.sleep(1)
    pyautogui.press('r')#resume the ad
    time.sleep(15)
    scroll_up()
    #os.system(bashCommand)
    close_tab()

def incontent_auto(i):
    b.open(i,new=new)
    time.sleep(3)
    scroll_down()
    ad_spotter()
    time.sleep(5)
    pyautogui.press('p')
    time.sleep(2)
    pyautogui.press('r')
    time.sleep(15)
    full_screen()
    pyautogui.press('esc')
    scroll_up()
    #os.system(bashCommand)
    close_tab()

def instream_noauto(i):
    b.open(i,new=new)
    time.sleep(3)
    pyautogui.press('s')#starts the ad
    time.sleep(2)
    #pyautogui.click('')#write this out to clickthrough
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
    time.sleep(15)
    #os.system(bashCommand)
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')

def instream_auto(i):
    b.open(i,new=new)
    time.sleep(3)
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
    #os.system(bashCommand)
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')

def main():

    for i in file1:
        #try:
        if 'incontent' and 'spotx_autoplay=0' in i:
            incontent_noauto(i)
        elif 'instream' and 'spotx_autoplay=0' in i:
            instream_noauto(i)
        elif 'instrem' and 'spotx_autoplay=&' in i:
            instream_auto(i)
        '''except KeyboardInterrupt: 
            print ("\nPausing... (Hit ENTER to continue, type quit to exit, or c to copy the url to the failed file.)")
            try:
                response = raw_input()
                if response == 'quit':
                    exit()
                elif response == 'c':
                    with open('problem.txt', 'a') as f:
                        f.write(i+'\n')
                        continue
            except KeyboardInterrupt:
                print ('Resuming...')
                continue'''
main()
    

    
    

