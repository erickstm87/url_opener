#!/usr/bin/python
import webbrowser
import csv
import numpy as np

new_file = []
file1 = open('text.txt')
for row in file1:
	new_file.append(row)
np.transpose(new_file)
print(new_file)