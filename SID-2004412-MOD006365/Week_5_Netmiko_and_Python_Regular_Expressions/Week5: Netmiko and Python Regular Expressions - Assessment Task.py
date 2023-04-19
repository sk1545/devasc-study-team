# SID: 2004412 - MOD006365

# The purpose of this task is to obtain the output of the "show version" command and display the output within the terminal

# First, the Netmiko Python library is imported into the file.

from netmiko import Netmiko

# Dictionary named "cisco1" stores information about the CSR1000v router including IP address, username and passwords, as well as device type.
cisco1 = {
    "host": "192.168.56.105",
    "username": "cisco",
    "password": "cisco123!",
    "device_type": "cisco_ios",
}

# net_connect is a python module with the netmiko library to connect to network devices.
# In this case, the parameters specified in the dictionary above are being used to access the CSR1000v router.
net_connect = Netmiko(**cisco1)
command = "show version"
# the "command = "show version" is teh command used to obtain version information from the router. 

print()
# The below line is a funtion which returns the current current prompt of the network device.
print(net_connect.find_prompt())
# The below line is executing the command specified earlier on the CSR1000v router. 
output = net_connect.send_command(command)
# The below line is disconnecting connection to the CSR1000v router. 
net_connect.disconnect()
# Below is code to display the output from the CSR1000v router.
print(output)
print()

