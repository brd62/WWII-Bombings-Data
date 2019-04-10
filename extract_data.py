
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
	item["TGTCOUNTRY"] = i["TGTCOUNTRY"]
	item["TGTLOCATION"] = i["TGTLOCATION"]
	item["COUNTRY"] = i["COUNTRY"]
	item["NUMBEROFPLANESATTACKING"] = i["NUMBEROFPLANESATTACKING"]
	item["MDS"] = i["MDS"] 
	output.append(item)


with open('ww1_data.json', 'w') as outfile:
    json.dump(output, outfile)

#World war 2

output2 = []
temp_list = []
countries = []

with open('wwII.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = True
    bogusValues = ["", "null", "UNKNOWN OR NOT INDICATED", "UNIDENTIFIED", "undefined", "UNIDENTIFIED TARGETS", "UNIDENTIFIED TARGET"]
    for row in readCSV:
    	if first==True:
    		first = False
    		continue
    	else:
    		if row[5] not in bogusValues and row[17] not in bogusValues and row[16] not in bogusValues and row[7] not in bogusValues and row[8] not in bogusValues:
		    	item = row[5]+ "," + row[7]+ "," + row[8]+ "," + row[15]+ "," + row[16]+ "," + row[2]+","+row[16]+","+row[17]
		    	output2.append(item)

final_out = set(output2)
final_out2 = []
final_out2.append(["COUNTRY_FLYING_MISSION","TGT_COUNTRY","TGT_LOCATION", "LATITUDE", "MSNDATE","TGT_TYPE","TGT_INDUSTRY"])
for i in final_out:
	item = i.split(",")
	final_out2.append(item)


with open('ww2_data.csv', "wb") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(final_out2)



