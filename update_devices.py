import sys
import csv
import paramiko
import pyperclip
import ipaddress
cmd_1="nvram set static_leasenum="
cmd_2="nvram set static_leases="
leases=[]
with open('devices.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            # get variables
            name = row['FULLID']
            mac = row['MAC']
            ip = row['IP']
            # do not add non-connected devices
            if len(mac) != 17:
                continue
            # fix ip format
            ip = '.'.join(ip.split('.')[:-1])+'.'+str(int(ip.split('.')[-1]))
            # add lease
            leases.append((mac, name, ip))
# format
leases_str="= ".join(["=".join(x) for x in leases])
cmd_1=cmd_1+str(len(leases))
cmd_2=cmd_2+'"'+leases_str+'"'
pyperclip.copy(cmd_1+'\n'+cmd_2)
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
# client.connect(sys.argv[1], username=sys.argv[2], password=sys.argv[3])
# client.exec_command(cmd_1)
# client.exec_command(cmd_2)
# client.close()
