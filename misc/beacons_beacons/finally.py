import csv 
#os.system('mv /home/vagrant/repositories/beacon_types.txt .')
reader = csv.reader(open('my_webs.csv','rb'))
reader1 = csv.reader(open('beacon_results.csv','rb'))
writer = csv.writer(open('appended_output.csv','wb'))
for row in reader:
	row1 = reader1.next()
	writer.writerow(row + row1)