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

pyautogui.size()
width,height = pyautogui.size()
b_rowser = input('do you want to run this in safari, chrome, or firefox? Make sure to type your choice exactly as it appears \n')
if b_rowser == 'safari':
    b = webbrowser.get('safari')
    bashCommand = "sudo killall 'Safari' "
elif b_rowser == 'chrome':
    b = webbrowser.get()
    bashCommand = "sudo killall 'google' "
elif b_rowser == 'firefox':
    b = webbrowser.get('firefox')
    bashCommand = "sudo killall 'firefox' "
new = 1
file1 = open('bright_urls.txt', 'r')
x = 0

def ad_spotter(i):
    try:
        x,y = pyautogui.locateCenterOnScreen('jira.png')
        l,s = (int(x/2),int(y/2))
        pyautogui.moveTo(l,s)
        pyautogui.click(l,s)
        time.sleep(2)
        #pyautogui.click(l,s)
        #print(l,s)
        return(l,s)
    except:
        type=='NoneType'
        print('couldnt find play icon')
        with open('problem_b.txt', 'a') as f:
            f.write('COULDNT FIND PLAY ICON'+ i+'\n')
            return
    
def full_screen(i):
    try:
        x,z = resume()
        print('full_screen returns %s %s as coordinates for resume' %(x,z))
        i,f = (847+x,z)
        print(i,f)
        pyautogui.moveTo(i,f)
        time.sleep(1)
        pyautogui.click(i,f)
        time.sleep(1)
        pyautogui.press('esc')
        pyautogui.press('esc')
    except:
        type == 'NoneType'
        with open('problem_b.txt', 'a') as f:
            f.write('FULL SCREEN NOT FOUND'+ i+'\n')
            
def resume():
    try:
        #print('running resume')
        f,g = pyautogui.locateCenterOnScreen('play.png')
        r,f = (int(f/2),int(g/2))
        #print(r,f)
        pyautogui.moveTo(r,f)
        pyautogui.click(r,f)
        print(r,f)
        return(r,f)
    except:
        if type=="NoneType":
            print('couldnt find it')
            with open('problem_b.txt', 'a') as f:
                f.write('COULDNT FIND THE RESUME PLAY ICON' + i+'\n')
            return
def click_through(i):
    try:
        print('click_through is running')
        x,y = ad_spotter(i)
        pyautogui.click(x,y)
        time.sleep(2)
        pyautogui.click(x,y)
        time.sleep(2)
        close_tab()
    except:
        if type=="NoneType":
            print('couldnt click through')
            with open('problem_b.txt', 'a') as f:
                f.write('COULDNT CLICK THROUGH' +i+'\n')
        return
    
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
        with open('problem_b.txt', 'a') as f:
                        f.write('SLOT ISSUE,'+ i+'\n')'''

def brightcove_noauto(i):
    b.open(i,new=new)
    time.sleep(2)
    #ad_spotter(i)
    click_through(i)
    #x,z = resume()
    full_screen(i)
    time.sleep(9)
    close_tab()

def brightcove_auto(i):
    b.open(i,new=new)
    time.sleep(2)
    click_through(i)
    full_screen()
    time.sleep(9)
    close_tab()
   
def main():
    #click_through()
    #(x,z) = resume()
    #print(x,z)
    #full_screen(x,z)
    #full_screen(x)
    das_auto = input('are these urls autoplay or not? type out yes or no \n')
    for i in file1:
        try:
            if das_auto == 'yes':
                brightcove_auto(i)
            elif das_auto == 'no':
                brightcove_noauto(i)
        except KeyboardInterrupt: 
            print ("\nPausing... (Hit ENTER to continue, type quit to exit, or copy to copy the url to the failed file.)")
            try:
                response = input()
                if response == 'quit':
                    #os.system(bashCommand)
                    quit()
                elif response == 'copy':
                    message = input('would you like to submit an error message with the URL? type out yes or no \n')
                    if message == 'yes':
                        e_message = input('what would you like your message to be? \n')
                        with open('problem_b.txt', 'a') as f:
                            f.write(e_message.upper()+'\n'+ i+'\n')
                            #os.system(bashCommand)
                            continue
                    elif message == 'no':
                        with open('problem_b.txt', 'a') as f:
                            f.write(i+'\n')
                            os.system(bashCommand)
                            continue
                    else:
                        print ('Resuming...')
                        os.system(bashCommand)
                        continue
            except KeyboardInterrupt:
                print ('resuming')
                os.system(bashCommand)
                continue
main()
    

    
    

