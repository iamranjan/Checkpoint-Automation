
import paramiko
import pandas as pd
a=pd.read_excel('Firewall_list.xlsx')
rows=a.shape[0]
h=a['Hostname']
p=a['Password']
commands=['clish -c "lock database override"','clish -c "show asset all"','clish -c "show configuration"','clish -c "cphaprob stat"',
          'clish -c "show configuration static-route"','clish -c "fw getifs"','clish -c "show route"',
         'clish -c "show configuration interface"','clish -c "show interfaces all"','cphaprob stat','fw stat']
print ("welcome to Python Automatic Backup tool. Now you will see the commands that are running in the background \n")


for i in range(0,rows):
    paramiko.util.log_to_file('ssh_connections.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(h[i], 22, 'admin', p[i])
    with open(f'{h[i]}.txt', 'w') as f:
        print(f'Backup of Firewall having {h[i]} is as follows \n', file=f) 
    for j in commands:
        print(f'Command{j}')
        stdin, stdout, stderr = s.exec_command(j)
        a=stdout.read()
        b=str(a,'utf-8')
        with open(f'{h[i]}.txt', 'a') as f:
            print(f'{j}\n {b}\n', file=f)
print (f"File saved with the name of {h[i]}")







