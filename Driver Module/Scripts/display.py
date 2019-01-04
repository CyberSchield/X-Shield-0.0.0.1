def display(process_list):
	for p in process_list:
		print(str(p.process_id)+"    "+str(p.ram_usage)+"   "+str(p.cpu_usage)+"     "+str(p.process_priority)+"     "+str(p.user_type)+"      "+str(p.process_state))
