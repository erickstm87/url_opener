#!/usr/bin/python
import webbrowser
import csv
import numpy as np
import sys

b = webbrowser.get('firefox')
new_file = []
file1 = open('text.txt')
for row in file1:
	new_file.append(row)
np.transpose(new_file)
for i in new_file:
    b.open(i)
#sys.stdout = open('link.txt','w')
#print(new_file)
