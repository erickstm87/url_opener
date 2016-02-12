#!/usr/bin/python
import webbrowser
import csv
import numpy as np

b = webbrowser.get('firefox')
with open ('link.csv', 'rb') as f:
	reader = csv.reader(f)
	f1 = list(reader)
	print type(f1)
	for x in f1:
		print(x)
		b.open(x)