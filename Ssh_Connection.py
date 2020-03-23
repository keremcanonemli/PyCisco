#Bu script içerisinde ip address'i bilinen bir cihaza ssh bağlantısı yapmanın komutları bulunmaktadır
from netmiko import ConnectHandler
SW1 = {
    'device_type': 'cisco_ios',
    'host':   '10.0.10.12',
    'username': 'admin',
    'password': 'Btegitim2020',
    'port' : 22,          # optional, defaults to 22
    'secret': 'Btegitim2020',     # optional, defaults to ''
}
try:
    net_connect = ConnectHandler(**SW1)
    print("Successful")
except Exception as ex:
    print(ex)
