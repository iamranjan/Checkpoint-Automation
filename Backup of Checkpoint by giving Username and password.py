
import paramiko
import pandas as pd
import datetime
import getpass
print ("Welcome to Python Automatic Backup of configuration tool. PLease share required information below\n") 
h=input("Enter the IP Address of the Firewall\n")
p=getpass.getpass("Enter the Password of the Firewall\n")
port=input("Enter the opened port of the Firewall\n")
commands=['clish -c "lock database override"','clish -c "show asset all"','clish -c "show configuration"','clish -c "cphaprob stat"',
          'clish -c "show configuration static-route"','clish -c "fw getifs"','clish -c "show route"',
         'clish -c "show configuration interface"','clish -c "show interfaces all"','cphaprob stat','fw stat']

print ("Now you will see the commands that are running in the background \n")
import time
paramiko.util.log_to_file('ssh_connections.log')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(h,port, 'admin', p)
z=time.strftime("%Y%m%d-%H%M%S")

with open(f'{h}{z}.txt', 'w') as f:
       print(f'Backup of Firewall having {h} is as follows \n', file=f) 
for j in commands:
    print(f'Command ## {j}')
    stdin, stdout, stderr = s.exec_command(j)
    a=stdout.read()
    b=str(a,'utf-8')
    with open(f'{h}{z}.txt', 'a') as f:
        print(f'{j}\n {b}\n', file=f)
print (f"File saved with the name of {h}{z}.txt")



