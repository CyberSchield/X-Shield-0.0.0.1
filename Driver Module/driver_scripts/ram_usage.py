import subprocess
def ram_usage(pid):
	temp=subprocess.Popen(['ps','-o','%mem','-p',str(pid)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	ram_usage=str(temp.stdout.read())[8:-3].strip()
	if ram_usage=="":
		ram_usage=0.0
	else:
		ram_usage=float(ram_usage)
	return ram_usage
