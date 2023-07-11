# This tool is for subnet calculation.

# Subnet Tool

The Subnet Tool is a command-line utility written in Python that helps you calculate the network, broadcast, first, and last host addresses in a subnet. It also provides a colorful ASCII art banner to enhance the tool's appearance.

## Prerequisites

Before using the Subnet Tool, make sure you have the following prerequisites installed:

- Python 3: If you don't have Python 3 installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Installation

1. Download the Subnet Tool code from the repository: [https://github.com/your-username/subnet-tool](https://github.com/your-username/subnet-tool)
2. Open a terminal or command prompt.
3. Navigate to the directory where the Subnet Tool code is saved.

## Setup

1. Create a virtual environment (optional but recommended):
   - Run `python3 -m venv subnet-env` to create a virtual environment named "subnet-env".
   - Activate the virtual environment:
     - For Windows: Run `subnet-env\Scripts\activate.bat`
     - For macOS/Linux: Run `source subnet-env/bin/activate`

2. Install the required dependencies:
   - Run `pip install -r requirements.txt` to install the required packages: argparse, ipaddress, pyfiglet, termcolor, tabulate.

## Usage

To execute the Subnet Tool in the terminal, use the following command:

Replace `<IP_ADDRESS>` with the IP address you want to calculate the subnet for and `<SUBNET_MASK>` with the subnet mask in CIDR notation (e.g., 24).

For example, to calculate the subnet information for IP address `192.168.0.10` with a subnet mask of `24`, run the following command:


