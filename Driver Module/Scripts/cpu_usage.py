import subprocess
def cpu_usage(pid):
	temp=subprocess.Popen(['ps','-o','%cpu','-p',str(pid)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	cpu_usage=str(temp.stdout.read())[8:-3].strip()
	if cpu_usage=="":
		cpu_usage=0.0
	else:
		cpu_usage=float(cpu_usage)
	return cpu_usage
