from netmiko import ConnectHandler
import time
import multiprocessing as mp
import getpass
import logging
import os
import re
import logging.handlers
from ssh_netmiko import *
logger_root = os.environ['LOGGER'] if 'LOGGER' in os.environ else 'robot_frameworkLog'
logger = logging.getLogger(f'{logger_root}.{__name__}')




class Router:
    def __init__(self,ssh,hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.cdp_neighbor = []
        self.platform = ''
        self.ssh  = ssh_connection(hostname, username, password)

    @property
    def modules(self):
        show_platform = self.cli(['show platform'], screen=False).split('\r\n')
        return show_platform

    def refresh_ssh(self):
        self.ssh = ssh_connection(hostname, username, password)

    def get_show_run(self):
        output = cli(ssh_connection,commands='show run')
        return output

    def connect(self, hostname=None, username=None, password=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        try:
            ssh_connection(self.hostname, self.username, self.password)
        except Exception as e:
            logger.warning(f'Error connecting SSH to {self.hostname}')
            logger.warning(e)

    def cli(ssh_connection,hostname, command=None, log_file='', screen=True, banner=''):
        output = cli(ssh_connection,hostname,command, log_file=log_file, banner=banner)
        return output
    def configure_ip_address(hostname):

        if hostname in data["Devices"]:
             print(f'Start configure ip on {hostname}')
             if hostname == 'R1':
                 try:
                       assert  hostname == 'R1'
                       print('=_=_='*10)
                       Mgmt_ip = data["Devices"][hostname]["ip_address"]
                       loopback0 = data["Devices"][hostname]["loopback0"] + ' ' + data["Devices"][hostname]["mask32"]
                       interface_Gi2 = data["Devices"][hostname]["Gi2"] + ' ' + data["Devices"][hostname]["mask"]
                       interface_Gi3 = data["Devices"][hostname]["Gi3"] + ' ' + data["Devices"][hostname]["mask"]
                       config = '''
                       interface lo0
                       ip address {}
                       exit
                       interface Gi2
                       ip address {}
                       no shut
                       exit
                       interface Gi3
                       ip address {}
                       no shut
                       exit'''.format(loopback0,interface_Gi2, interface_Gi3).lstrip().rstrip().split('\n')

                       cisco_device = {
                           'device_type': 'cisco_ios',
                           'ip': Mgmt_ip,
                           'username': 'admin',
                           'password': 'cisco',
                           'verbose': True
                       }
                       conn = ConnectHandler(**cisco_device)
                       conn.enable()
                       commands= config
                       output = conn.send_config_set(commands)
                       print('=_=_='*10)
                       print(f'Pushing the following configuration on {hostname}')
                       print('=_=_='*10)
                       print(f'Configuring {output} on  router {hostname}')
                       print('=_=_='*10)
                       print(f'Saving configuration on {hostname}')
                       print('=_=_='*10)
                       output1 = conn.send_command_expect('write memory')
                       conn.disconnect()
                 except (AssertionError):

                       print('==='*10)
                       print(f"Device is not R1 either 'R2' or 'R3'")
                       print('==='*10)
             if hostname == 'R2':
                 try:
                     assert hostname == 'R2'
                     print('=_=_=' * 10)
                     Mgmt_ip = data["Devices"][hostname]["ip_address"]
                     loopback0 = data["Devices"][hostname]["loopback0"] + ' ' + data["Devices"][hostname]["mask32"]
                     interface_Gi2 = data["Devices"][hostname]["Gi2"] + ' ' + data["Devices"][hostname]["mask"]
                     config = '''
                     interface lo0
                     ip address {}
                     exit
                     interface Gi2
                     ip address {}
                     no shut
                     exit'''.format(loopback0, interface_Gi2).lstrip().rstrip().split('\n')

                     cisco_device = {
                         'device_type': 'cisco_ios',
                         'ip': Mgmt_ip,
                         'username': 'admin',
                         'password': 'cisco',
                         'verbose': True
                     }
                     conn = ConnectHandler(**cisco_device)
                     conn.enable()
                     commands = config
                     output = conn.send_config_set(commands)
                     print('=_=_=' * 10)
                     print(f'Pushing the following configuration on {hostname}')
                     print('=_=_=' * 10)
                     print(f'Configuring {output} on  router {hostname}')
                     print('=_=_=' * 10)
                     print(f'Saving configuration on {hostname}')
                     print('=_=_=' * 10)
                     output1 = conn.send_command_expect('write memory')
                     conn.disconnect()
                 except(AssertionError):
                     print('===' * 10)
                     print(f"device is not R2 its   'R3'")
                     print('===' * 10)
             if hostname == 'R3':
                 try:
                       assert hostname == 'R3'
                       print('=_=_=' * 10)
                       Mgmt_ip = data["Devices"][hostname]["ip_address"]
                       loopback0 = data["Devices"][hostname]["loopback0"] +' '+data["Devices"][hostname]["mask32"]
                       interface_Gi3 =  data["Devices"][hostname]["Gi3"]  +' '+data["Devices"][hostname]["mask"]
                       config = '''
                       interface lo0
                       ip address {}
                       exit
                       interface Gi3
                       ip address {}
                       no shut
                       exit'''.format(loopback0,interface_Gi3).lstrip().rstrip().split('\n')

                       cisco_device = {
                           'device_type': 'cisco_ios',
                           'ip': Mgmt_ip,
                           'username': 'admin',
                           'password': 'cisco',
                           'verbose': True
                       }
                       conn = ConnectHandler(**cisco_device)
                       conn.enable()
                       commands = config
                       output = conn.send_config_set(commands)
                       print('=_=_=' * 10)
                       print(f'Pushing the following configuration on {hostname}')
                       print('=_=_=' * 10)
                       print(f'Configuring {output} on  router {hostname}')
                       print('=_=_=' * 10)
                       print(f'Saving configuration on {hostname}')
                       print('=_=_=' * 10)
                       output1 = conn.send_command_expect('write memory')
                 except(AssertionError):
                      print('===' * 10)
                      print ('No Matching device found!! please choose a valid device name ')
                      print('===' * 10)

        else:
              print('Error, no valid device name ')
              exit()
    def configure_ospf(hostname):

        if hostname in data["Devices"]:
             print(f'Start adding OSPF on  {hostname}')
             if hostname == 'R1':
                 try:
                       assert  hostname == 'R1'
                       print('=_=_='*10)
                       Mgmt_ip = data["Devices"][hostname]["ip_address"]
                       loopback0 = data["Devices"][hostname]["loopback0"]
                       interface_Gi2 =   data["Devices"][hostname]["Gi2"]
                       interface_Gi3 =  data["Devices"][hostname]["Gi3"]
                       mask = data["Devices"][hostname]["mask"]
                       wild_card = data["Devices"][hostname]["Wmask"]
                       config = '''
                       router ospf 1
                       router-id  {0}
                       network {0} 0.0.0.0 area 0
                       network {1} {3} area 0
                       network {2} {3} area 0
                       exit'''.format(loopback0,interface_Gi2,interface_Gi3,wild_card).lstrip().rstrip().split('\n')

                       cisco_device = {
                           'device_type': 'cisco_ios',
                           'ip': Mgmt_ip,
                           'username': 'admin',
                           'password': 'cisco',
                           'verbose': True
                       }
                       conn = ConnectHandler(**cisco_device)
                       conn.enable()
                       commands= config
                       output = conn.send_config_set(commands)
                       print('=_=_='*10)
                       print(f'Pushing the following configuration on {hostname}')
                       print('=_=_='*10)
                       print(f'Configuring {output} on  router {hostname}')
                       print('=_=_='*10)
                       print(f'Saving configuration on {hostname}')
                       print('=_=_='*10)
                       output1 = conn.send_command_expect('write memory')
                       conn.disconnect()
                 except (AssertionError):

                       print('==='*10)
                       print(f"device is not R1 either 'R2' or 'R3'")
                       print('==='*10)
             if hostname == 'R2':
                 try:
                     assert hostname == 'R2'
                     print('=_=_=' * 10)
                     Mgmt_ip = data["Devices"][hostname]["ip_address"]
                     loopback0 = data["Devices"][hostname]["loopback0"]
                     interface_Gi2 = data["Devices"][hostname]["Gi2"]
                     mask = data["Devices"][hostname]["mask"]
                     wild_card = data["Devices"][hostname]["Wmask"]
                     config = '''
                       router ospf 1
                       router-id  {0}
                       network {0} 0.0.0.0 area 0
                       network {1} {2} area 0
                       exit'''.format(loopback0,interface_Gi2,wild_card).lstrip().rstrip().split('\n')

                     cisco_device = {
                         'device_type': 'cisco_ios',
                         'ip': Mgmt_ip,
                         'username': 'admin',
                         'password': 'cisco',
                         'verbose': True
                     }
                     conn = ConnectHandler(**cisco_device)
                     conn.enable()
                     commands = config
                     output = conn.send_config_set(commands)
                     print('=_=_=' * 10)
                     print(f'Pushing the following configuration on {hostname}')
                     print('=_=_=' * 10)
                     print(f'Configuring {output} on  router {hostname}')
                     print('=_=_=' * 10)
                     print(f'Saving configuration on {hostname}')
                     print('=_=_=' * 10)
                     output1 = conn.send_command_expect('write memory')
                     conn.disconnect()
                 except(AssertionError):
                     print('===' * 10)
                     print(f"device is not R2 its   'R3'")
                     print('===' * 10)
             if hostname == 'R3':
                 try:
                       assert hostname == 'R3'
                       print('=_=_=' * 10)
                       Mgmt_ip = data["Devices"][hostname]["ip_address"]
                       loopback0 = data["Devices"][hostname]["loopback0"]
                       interface_Gi3 =  data["Devices"][hostname]["Gi3"]
                       mask = data["Devices"][hostname]["mask"]
                       wild_card = data["Devices"][hostname]["Wmask"]
                       config = '''
                       router ospf 1
                       router-id  {0}
                       network {0} 0.0.0.0 area 0
                       network {1} {2} area 0
                       exit'''.format(loopback0,interface_Gi3,wild_card).lstrip().rstrip().split('\n')

                       cisco_device = {
                           'device_type': 'cisco_ios',
                           'ip': Mgmt_ip,
                           'username': 'admin',
                           'password': 'cisco',
                           'verbose': True
                       }
                       conn = ConnectHandler(**cisco_device)
                       conn.enable()
                       commands = config
                       output = conn.send_config_set(commands)
                       print('=_=_=' * 10)
                       print(f'Pushing the following configuration on {hostname}')
                       print('=_=_=' * 10)
                       print(f'Configuring {output} on  router {hostname}')
                       print('=_=_=' * 10)
                       print(f'Saving configuration on {hostname}')
                       print('=_=_=' * 10)
                       output1 = conn.send_command_expect('write memory')
                 except(AssertionError):
                      print('===' * 10)
                      print ('No Matching device found!! please choose a valid device name ')
                      print('===' * 10)

        else:
              print('Error, no valid device name ')
              exit()


if __name__ == '__main__':
    import doctest
    from pprint import pprint
    #x = Router.cli(ssh_connection,command='show version')
    # y = Router.configure_ip_address('R1')
    # n = Router.configure_ip_address('R2')
    # k = Router.configure_ip_address('R3')
    # test = Router.configure_ospf('R1')
    # test1 = Router.configure_ospf('R2')
    # test2 = Router.configure_ospf('R3')
    #     # print(x)
     doctest.testmod()

