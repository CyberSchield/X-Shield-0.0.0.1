import os,subprocess,process,display,ram_usage,cpu_usage

process_ids=list(os.popen("ps -o pid"))
process_ids.pop(0)
process_ids=[int(pid.strip()) for pid in process_ids]

process_list=[]

for pid in process_ids:

	ram_temp=ram_usage.ram_usage(pid)
	cpu_temp=cpu_usage.cpu_usage(pid)

	p=process.process(ram_temp,cpu_temp)	
	process_list.append(p)

display.display(process_list)




