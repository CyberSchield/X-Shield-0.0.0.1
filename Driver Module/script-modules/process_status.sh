#1/bin/bash
process_status=$(ps -o sgi_p,psr,sig,sigcatch,sigignore,sigmask -p $1)

echo "Process Status =$process_status"
