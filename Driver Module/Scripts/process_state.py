import subprocess
def process_state(pid):
	temp=subprocess.Popen(['ps','-o','stat','-p',str(pid)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	process_state=str(temp.stdout.read())[8:-3].strip()
	if process_state!="":
		process_state=process_state[0]
		if process_state=="D":#uninterruptible sleep
			return 0
		elif process_state=="R":#running or runnable
			return 1
		elif process_state=="S":#interruptible sleep
			return 2
		elif process_state=="T":#stopped
			return 3
		elif process_state=="W":#paging
			return 4
		elif process_state=="X":#dead
			return 5
		elif process_state=="Z":#defunct
			return 6
		else:
			return 5
	else:
		return 5
	print(process_state)
