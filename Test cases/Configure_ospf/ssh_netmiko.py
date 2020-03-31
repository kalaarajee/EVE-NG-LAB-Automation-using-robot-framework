from netmiko import ConnectHandler
import time
import multiprocessing as mp
import getpass
import logging
import os
import re
import logging.handlers
import json
import jsonpath
logger_root = os.environ['LOGGER'] if 'LOGGER' in os.environ else 'robot_frameworkLog'
logger = logging.getLogger(f'{logger_root}.{__name__}')
device_file = 'C:/Users/Kadhim/Desktop/Robot-framework/Test cases\Configure_ospf/devices.txt'
topology_json = 'C:/Users/Kadhim/Desktop/Robot-framework/Test cases/Configure_ospf/Topology.json'
with open(device_file, 'r') as f:
    device_list = f.read().split('\n')
with open(topology_json)  as jf:
    data = json.load(jf)


def ssh_connection(hostname, username, password):
    if ' ' in hostname + username + password:
        raise ValueError('Invalid input')
    conn = get_ssh_Netmiko(hostname, username, password)
    if conn is not None:
        conn.enable()
        conn.disconnect()

    else:
        print(f'Error connect to SSH to {hostname}')

def get_ssh_Netmiko(hostname, username, password):
    if ' ' in hostname + username + password:
        raise ValueError('Invalid input')

    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': hostname,
        'username': 'admin',
        'password': 'cisco',
        'verbose': True
    }
    conn = ConnectHandler(**cisco_device)
    conn.enable()
    conn.send_command('term width 0')
    return conn

def cli(ssh_connections, hostname,commands=None, log_file='', banner='', expect_string='#'):
    outputs = []
    if log_file:
        directory = os.path.dirname(os.path.abspath(log_file))
        if not os.path.exists(directory):
            os.makedirs(directory)
    if not isinstance(commands, list):
        command_list = [commands]

    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': hostname,
        'username': 'admin',
        'password': 'cisco',
        'verbose': True
    }
    conn = ConnectHandler(**cisco_device)
    conn.enable()
    conn.send_command('term width 0')
    conn.send_command_expect('#')
    output = conn.send_command(commands)
    outputs.append(output)
    conn.disconnect()
    return outputs

