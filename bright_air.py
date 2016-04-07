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
#sed command to eliminate all iframes on the urls (sed -i -e 's/iframe=./iframe=0/g')

#file1 = input('whats the filename of your urls? make sure its a txt file, you dont need to type in the file extension \n') + '.txt'

new = 1
file1 = open('easi_urls.txt', 'r')
x = 0

pyautogui.size()
width,height = pyautogui.size()
b_rowser = raw_input('do you want to run this in safari, chrome, or firefox? Make sure to type your choice exactly as it appears \n')
if b_rowser == 'safari':
    b = webbrowser.get('safari')
    bashCommand = "sudo killall 'Safari' "
elif b_rowser == 'chrome':
    b = webbrowser.get()
    bashCommand = "sudo killall 'google' "
elif b_rowser == 'firefox':
    b = webbrowser.get('firefox')
    new_file = []
    for row in file1:
        new_file.append(row)
        np.transpose(new_file)
        new_file = file1
#p.transpose(new_file)
    bashCommand = "sudo killall 'firefox' "


def scroll_downin():
    i = 0
    if b_rowser == 'safari':
        for i in range(0,7):
            pyautogui.press('down')
    elif b_rowser == 'firefox':
        for i in range(0,12):
            pyautogui.press('down')
    elif b_rowser == 'chrome':
        for i in range(0,15):
            pyautogui.press('down')

def instream_adspot(i):
    try:
        if b_rowser == 'safari':
            l = (os.path.abspath('/Users/terickson/url_opener/png_files/in_saf.png'))
        elif b_rowser == 'firefox':
            l = (os.path.abspath('/Users/terickson/url_opener/png_files/in_fire.png'))
        elif b_rowser == 'chrome':
            l = (os.path.abspath('/Users/terickson/url_opener/png_files/in_chrome.png')
        x,y = pyautogui.locateCenterOnScreen(l,grayscale=True,tolerance=10)
        bottom_play = ((x),(y-50))
        pyautogui.moveTo(bottom_play)
        pyautogui.click(bottom_play)
        return bottom_play
    except:
        type == 'NoneType'
        print('no ad could be found')
        with open('problem.txt', 'a') as f:
            f.write('NO AD FOUND'+ i+'\n')
            close_tab()
            main()

def ad_spotter(i): 
    try:
        if b_rowser == 'safari':
            l = ('saf_play.png')
        elif b_rowser == 'firefox':
            l = ('fire_play.png')
        elif b_rowser == 'chrome':
            l = ('chrome_play.png')
        x,y = pyautogui.locateCenterOnScreen(l)
        #r,s = (int(x/2),int(y/2))
        bottom_play = ((x-73),(y+309))
        #print(new_center)
        pyautogui.moveTo(bottom_play)
        pyautogui.click(bottom_play)
        return bottom_play
    except:
        type == 'NoneType'
        print('no ad could be found')
        with open('problem.txt', 'a') as f:
            f.write('NO AD FOUND'+ i+'\n')
            close_tab()
            main()

def full_screen(i):
    try:
        x,y = ad_spotter(i)
        l,s = (x+360,y)
        pyautogui.click(l,s)
        time.sleep(3)
        r,f = (l+20,s)
        pyautogui.moveTo(r,f)
    except:
        type == 'NoneType'
        print('couldnt find full screen')
        with open('problem.txt', 'a') as f:
            f.write('FULL SCREEN NOT FOUND'+ i+'\n')
            main()

def scroll_down():
    j = 0
    if b_rowser == 'safari':
        for j in range(0,30):
            pyautogui.press('down')
    elif b_rowser == 'firefox':
        for j in range(0,26):
            pyautogui.press('down')
    elif b_rowser == 'chrome':
        for j in range(0,33):
            pyautogui.press('down')
    #time.sleep(2)

def click_through(i):
    x,y = ad_spotter(i)
    l,s = (x+100,y-50)
    pyautogui.moveTo(l,s)
    time.sleep(2)
    for i in range(0,3):
        pyautogui.click(l,s)
    time.sleep(2)
    close_tab()

def scroll_up():
    j = 0
    for j in range(0,38):
        pyautogui.press('up')

def close_tab():
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')

'''def slots(i):
    if '92569' in i:
        try:
            foo = ['m_twitter.png','m_pinterest.png','m_facebook.png']
            slot = random.choice(foo)
            print(slot)
            x,y = pyautogui.locateCenterOnScreen((slot))
            x,y = int(x/2),(int(y/2))
            #pyautogui.moveTo(x,y)
            #pyautogui.click(x,y)
            print(x,y)
        except:
        type == 'NoneType'
        print('no ad could be found')
        with open('problem.txt', 'a') as f:
                        f.write('SLOT ISSUE,'+ i+'\n')'''

    
def incontent_noauto(i):
    b.open(i,new=new)
    time.sleep(3)
    scroll_down()
    time.sleep(1)
    pyautogui.press('s')
    time.sleep(2)
    pyautogui.press('m')#mute the ad
    pyautogui.press('v')#un-mute
    full_screen(i)
    time.sleep(1)
    pyautogui.press('esc')
    #pyautogui.click(810,409)
    #pyautogui.click(810,409)
    #pyautogui.click()
    pyautogui.click()
    pyautogui.press('s')
    pyautogui.press('r')
    click_through(i)
    pyautogui.press('p')#pause the ad
    time.sleep(1)
    pyautogui.press('r')#resume the ad
    pyautogui.click()
    time.sleep(15)
    scroll_up()
    #os.system(bashCommand)
    close_tab()

def incontent_auto(i):
    b.open(i,new=new)
    time.sleep(2)
    scroll_down()
    time.sleep(1)
    pyautogui.press('m')#mute the ad
    pyautogui.press('v')#un-mute
    full_screen(i)
    pyautogui.press('esc')
    #pyautogui.click(810,409)
    #pyautogui.click(810,409)
    pyautogui.click()
    pyautogui.click()
    pyautogui.press('s')
    pyautogui.press('r')
    click_through(i)
    time.sleep(3)
    pyautogui.press('p')
    time.sleep(2)
    pyautogui.press('r')
    pyautogui.click()
    time.sleep(15)
    scroll_up()
    #os.system(bashCommand)
    close_tab()

def instream_noauto(i):
    b.open(i,new=new)
    time.sleep(2)
    scroll_downin()
    time.sleep(3)
    pyautogui.press('s')#starts the ad
    time.sleep(2)
    pyautogui.press('p')#pause the ad
    time.sleep(1)
    pyautogui.press('r')#resume the ad
    time.sleep(1)
    pyautogui.press('m')
    time.sleep(1)
    pyautogui.press('v')
    click_through(i)
    pyautogui.press('r')
    full_screen(i)
    pyautogui.press('esc')
    time.sleep(10)
    #os.system(bashCommand)
    close_tab()

def instream_auto(i):
    b.open(i,new=new)
    time.sleep(2)
    scroll_downin()
    pyautogui.press('p')#pause the ad
    time.sleep(1)
    pyautogui.press('r')#resume the ad
    pyautogui.press('m')
    time.sleep(1)
    pyautogui.press('v')
    click_through(i)
    time.sleep(2)
    full_screen(i)
    time.sleep(10)
    #os.system(bashCommand)
    close_tab()

def main():
    for i in file1:
        try:
            if 'incontent' and 'spotx_autoplay=0' in i:
                incontent_noauto(i)
            elif 'inconent' and 'spotx_autoplay=&' in i:
                incontent_auto(i)
            elif 'instream' and 'spotx_autoplay=0' in i:
                instream_noauto(i)
            elif 'instrem' and 'spotx_autoplay=&' in i:
                instream_auto(i)
        except KeyboardInterrupt: 
            print ("\nPausing... (Hit ENTER to continue, type quit to exit, or copy to copy the url to the failed file.)")
            try:
                response = raw_input()
                if response == 'quit':
                    bashCommand = "sudo killall 'python'"
                    os.system(bashCommand)
                elif response == 'copy':
                    e_message = raw_input('what would you like your message to be? \n')
                    with open('problem.txt', 'a') as f:
                        f.write(e_message.upper()+','+ i+'\n')
                        os.system(bashCommand)
                        continue
            except KeyboardInterrupt:
                print 'Resuming...'
                continue
main()
    

    
    

