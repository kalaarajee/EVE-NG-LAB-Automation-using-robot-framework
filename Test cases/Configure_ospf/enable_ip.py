from Router import  *
from pprint import pprint
import json

'''
This playbook will use Router.py script to configure ip address 
'''

def enable_ssh(device):
    output = Router.connect(ssh_connection,device,'admin','cisco')
    return 'ssh session established!!'

def cli(device,command):
    output = Router.cli(ssh_connection,device,command)
    pprint(output)
def enable_ip(hostname):
    output = Router.configure_ip_address(hostname)



def enable_ospf(hostname):
    output = Router.configure_ospf(hostname)

if __name__ == '__main__':
    for hostname in data["Devices"]:
    #      print(hostname)
           output = enable_ip(hostname)
           output1 = enable_ospf(hostname)
    for device in device_list:
         #output2 = enable_ssh(device)
         output2 = cli(device, 'show ip int bri |  exc unass')
         output3 = cli(device,'show ip ospf neigh')
         pprint(f'show ip interface breif {output2}', widht=40)
         pprint(f'show ip ospf neighbor {output3}',width=40)