import os,subprocess,process,display,ram_usage,cpu_usage,process_priority,user_type,process_state

process_ids=list(os.popen("ps -o pid"))
process_ids.pop(0)
process_ids=[int(pid.strip()) for pid in process_ids]

process_list=[]

for pid in process_ids:

	ram_temp=ram_usage.ram_usage(pid)
	cpu_temp=cpu_usage.cpu_usage(pid)
	process_priority_temp=process_priority.process_priority(pid)	
	user_type_temp=user_type.user_type(pid)
	process_state_temp=process_state.process_state(pid)

	p=process.process(pid,ram_temp,cpu_temp,process_priority_temp,user_type_temp,process_state_temp)	
	process_list.append(p)

display.display(process_list)




