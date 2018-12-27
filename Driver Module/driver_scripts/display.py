def display(process_list):
	for p in process_list:
		print(str(p.ram_usage)+"   "+str(p.cpu_usage))
