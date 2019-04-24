import csv,os

def csvCreator(process_list):
	row=["cpu_usage","ram_usage","user_type","process_priority","process_state"]
	with open('Data.csv','a') as csvFile:
		writer=csv.writer(csvFile)
		#if os.stat('Data.csv').st_size==0:
		#	writer.writerow(row)
		for p in process_list:
			row=[p.cpu_usage,p.ram_usage,p.user_type,p.process_priority,p.process_state]
			writer.writerow(row)
	csvFile.close()
