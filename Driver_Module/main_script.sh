#!/bin/bash

present_active_process=$(ps -o pid)

  ### Activating the scripts
''' exec chmod 755 ./script-modules/command_executed.sh
exec chmod 755 ./script-modules/cpu-usage.sh
exec chmod 755 ./script-modules/Network-Bendwidth.sh
exec chmod 755 ./script-modules/process_port.sh
exec chmod 755 ./script-modules/process_priority.sh
exec chmod 755 ./script-modules/process_status.sh
exec chmod 755 ./script-modules/process_user.sh
exec chmod 755 ./script-modules/Ram-usage.sh
exec chmod 755 ./script-modules/read_write_status.sh '''

  ### basic script execution module 
while(true)
do
for p in $present_active_process:
do
   export p
   bash ./script-modules/command_executed.sh "$p"
   echo "***********************************"
   bash ./script-modules/cpu-usage.sh "$p"
   echo "***********************************"
   bash ./script-modules/process_port.sh TCP 8080
   echo "***********************************"
   bash ./script-modules/process_priority.sh "$p"
   echo "***********************************"
   bash ./script-modules/process_status.sh "$p"
   echo "***********************************"
   bash ./script-modules/process_user.sh "$p"
   echo "***********************************"
   bash ./script-modules/Ram-usage.sh "$p"
   echo "***********************************"
   bash ./script-modules/read_write_status.sh "$p"
   echo "***********************************"
   #bash ./script-modules/Network-Bendwidth.sh $p
   echo "***********************************"
done
sleep 5
done
