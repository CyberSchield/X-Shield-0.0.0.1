import subprocess
def process_priority(pid):
	temp=subprocess.Popen(['ps','-o','pri','-p',str(pid)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	process_priority=str(temp.stdout.read())[8:-3].strip()
	if process_priority=="":
		process_priority=20
	else:
		process_priority=int(process_priority)
	return process_priority
