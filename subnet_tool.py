#!/usr/bin/env python3

import argparse
import ipaddress
import pyfiglet
from termcolor import colored

def calculate_host_addresses(ip_address, subnet_mask):
    ip_network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    network_address = ip_network.network_address
    broadcast_address = ip_network.broadcast_address
    first_host = network_address + 1
    last_host = broadcast_address - 1
    return network_address, broadcast_address, first_host, last_host

# Create the argument parser
parser = argparse.ArgumentParser(prog='subnet_tool', description="Calculate network, broadcast, first and last host addresses in a subnet")
parser.add_argument('-p', '--ip', required=True, help='IP address')
parser.add_argument('-s', '--subnet', required=True, help='Subnet mask')

# Parse the command-line arguments
args = parser.parse_args()

ip_address = args.ip
subnet_mask = args.subnet

network_address, broadcast_address, first_host, last_host = calculate_host_addresses(ip_address, subnet_mask)

# Generate ASCII art banner
banner = pyfiglet.figlet_format("SUBNET_TOOL", font="slant")
colored_banner = colored(banner, color='cyan')

# Format the subnet information with colors
network_info = colored(f"Network Address: {network_address}", color='green')
broadcast_info = colored(f"Broadcast Address: {broadcast_address}", color='yellow')
first_host_info = colored(f"First Host: {first_host}", color='blue')
last_host_info = colored(f"Last Host: {last_host}", color='magenta')

# Print the banner and subnet information
print(colored_banner)
print(network_info)
print(broadcast_info)
print(first_host_info)
print(last_host_info)
