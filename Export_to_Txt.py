from netmiko import ConnectHandler
SW1 = {
    'device_type': 'cisco_ios',
    'host':   '10.0.10.20',
    'username': 'admin',
    'password': 'Btegitim2020',
    'port' : 22,          # optional, defaults to 22
    'secret': 'Btegitim2020',     # optional, defaults to ''
}
net_connect = ConnectHandler(**SW1)

showrun=net_connect.send_command("show running-config")
try:
    dosya = open("showrun.txt","w+")
    dosya.write(showrun)
except Exception as ex:
    print(ex)
