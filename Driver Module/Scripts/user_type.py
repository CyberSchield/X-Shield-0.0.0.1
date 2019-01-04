import subprocess
def user_type(pid):
	temp=subprocess.Popen(['ps','-o','user','-p',str(pid)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	user_type=str(temp.stdout.read())[8:-3].strip()
	if user_type=="" or user_type=="root":
		user_type=1
	else:
		user_type=0
	return user_type
