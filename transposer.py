#!/usr/bin/python
import webbrowser
import csv
import numpy as np
import sys
import os
import time

b = webbrowser.get('firefox')
#bashCommand = "/bin/bash kill.sh"
#bashCommand = "sudo killall 'Safari' "
bashCommand = "sudo killall -r 'firefox'"
new = 2
new_file = []
file1 = open('text.txt')
for row in file1:
	new_file.append(row)
np.transpose(new_file)
x = 0
for i in new_file:
    b.open(i,new=new)
    #webbrowser.open(i,new=new)
    time.sleep(5)
    os.system(bashCommand)
    x += 1
    print(x) 
    
    

