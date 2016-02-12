#!/usr/bin/python
import webbrowser
import csv
import numpy as np

b = webbrowser.get('firefox')
f = open('link.txt','r') 
list('f')
for j in f:
	print(j)
	b.open(j)
