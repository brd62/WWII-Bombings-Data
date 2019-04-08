
import sys, json
import csv

#World war 1


struct = []
try: #try parsing to dict
	p = 'ww1.json'
	with open(p, 'r') as f:
		data = json.loads(f.read())
except:
	print sys.exc_info()

output = []

for i in data:
	item = {}
	item["LATITUDE"] = i["LATITUDE"]
	item["LONGITUDE"] = i["LONGITUDE"]
	item["MSNDATE"] = i["MSNDATE"]
	output.append(item)


with open('ww1_data.json', 'w') as outfile:
    json.dump(output, outfile)

#World war 2

output2 = []


with open('wwII.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = True
    for row in readCSV:		
		item = [row[5],row[7],row[8],row[15],row[16],row[2]]
		#print(item)
		output2.append(item)

with open('ww2_data.csv', "wb") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(output2)



