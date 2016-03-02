#!/usr/bin/env python
import webbrowser
import csv
import numpy as np
import sys
import os
import time
import pyautogui
from subprocess import call
import random
#for installation of pyautogui on mac check out http://stackoverflow.com/questions/35051580/phyton3-pip-and-pyautogui-install-mac-remove-broken-python and go to the bottom 

pyautogui.size()
width,height = pyautogui.size()
'''b_rowser = input('do you want to run this in safari, chrome, or firefox? Make sure to type your choice exactly as it appears \n')
if b_rowser == 'safari':
    b = webbrowser.get('safari')
    bashCommand = "sudo killall 'Safari' "
elif b_rowser == 'chrome':
    b = webbrowser.get()
    bashCommand = "sudo killall 'google' "
elif b_rowser == 'firefox':
    b = webbrowser.get('firefox')
    bashCommand = "sudo killall 'firefox' "'''

new = 1
file1 = open('incon.txt', 'r')
#file1 = raw_input('whats the filename of your urls? make sure its a txt file, you dont need to type in the file extension \n') + '.csv'
x = 0

def ad_spotter():
    try:
        x,y = pyautogui.locateCenterOnScreen('ad_1.png')
        l,s = (int(x/2),int(y/2))
        new_center = ((l+125),(s+125))
        pyautogui.moveTo(new_center)
        pyautogui.click(new_center)
    except:
        type == 'NoneType'
        print('no ad could be found')
        with open('problem.txt', 'a') as f:
                        f.write(i+'\n'+' URL PROBLEM')
        main()

def full_screen():
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('full_screen.png')
    pyautogui.click(x,y)
    time.sleep(3)

def scroll_down():
    j = 0
    if b_rowser == 'safari':
        for j in range(0,37):
            pyautogui.press('down')
    elif b_rowser == 'firefox':
        for j in range(0,26):
            pyautogui.press('down')
    elif b_rowser == 'chrome':
        for j in range(0,29):
            pyautogui.press('down')
    time.sleep(2)

def click_through():
    ad_spotter()
    for i in range(0,3):
        pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    close_tab()

def scroll_up():
    j = 0
    for j in range(0,38):
        pyautogui.press('up')

def close_tab():
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')

def slots(i):
    if '92569' in i:
        try:
            foo = ['m_twitter.png','m_pinterest.png','m_facebook.png']
            slot = random.choice(foo)
            print(slot)
            x,y = pyautogui.locateCenterOnScreen((slot))
            x,y = int(x/2),(int(y/2))
            print(x,y)
            #pyautogui.moveTo(x,y)
            #pyautogui.click(x,y)
    '''elif '95772' in i:
        try:
            foo = []'''

def incontent_noauto(i):
    b.open(i,new=new)
    time.sleep(3)
    scroll_down()
    pyautogui.press('s')
    time.sleep(2)
    click_through()
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
    time.sleep(2)
    full_screen()
    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(10)
    scroll_up()
    #os.system(bashCommand)
    close_tab()

def instream_noauto(i):
    b.open(i,new=new)
    time.sleep(3)
    pyautogui.press('s')#starts the ad
    time.sleep(2)
    #pyautogui.moveTo(630,668)#this is to go full screen
    #time.sleep(1)
    #pyautogui.press('esc')
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
    pyautogui.press('p')#pause the ad
    time.sleep(1)
    pyautogui.press('r')#resume the ad
    time.sleep(10)
    #os.system(bashCommand)
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')

def main():
    slots()
    '''for i in file1:
        try:
            if 'incontent' and 'spotx_autoplay=0' in i:
                incontent_noauto(i)
            elif 'instream' and 'spotx_autoplay=0' in i:
                instream_noauto(i)
            elif 'instrem' and 'spotx_autoplay=&' in i:
                instream_auto(i)
        except KeyboardInterrupt: 
            pyautogui.press('p')
            print ("\nPausing... (Hit ENTER to continue, type quit to exit, or c to copy the url to the failed file.)")
            try:
                response = input()
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
    

    
    

