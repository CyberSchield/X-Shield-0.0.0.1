import csv
def readDataCSVFile():
	process_list=[]
	with open("/home/yash/X-Shield-0.0.0.1-master/Data_Set/Data.csv",'r') as csvFile:
		reader=csv.reader(csvFile)
		for row in reader:
			p=[float(row[0]),float(row[1]),int(row[2]),int(row[3]),int(row[4])]
			process_list.append(p)
	csvFile.close()
	#del process_list[0]
	return process_list
