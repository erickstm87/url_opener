#!/usr/bin/python
import webbrowser
import csv

with open('link1.csv') as f:
	lis = [x.split() for x in f]
for x in zip(*lis)
	for y in x:
		print(y+'\t', end='')
		print('n')
'''new_file = []
b = webbrowser.get('firefox')
'''new_row = []
for row in file1:
	new_row.append(row)
	new_file.append(tuple(new_row))'''
for row in file1:
	new_file.append(row)
	zip(*new_file)
	print(new_file)'''