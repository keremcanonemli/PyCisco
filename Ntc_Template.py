from ntc_templates.parse import parse_output
from netmiko import ConnectHandler
import json
SW1 = {
    'device_type': 'cisco_ios',
    'host':   '10.0.10.20',
    'username': 'admin',
    'password': 'Btegitim2020',
    'port' : 22,
    'secret': 'Btegitim2020'
}
connect=ConnectHandler(**SW1)
vlan_output=connect.send_command("show vlan")

vlan_parsed = parse_output(platform="cisco_ios", command="show vlan", data=vlan_output)
print(json.dumps(vlan_parsed,indent=4))

#print(vlan_parsed)