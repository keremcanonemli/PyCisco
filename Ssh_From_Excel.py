#cell_value rowx,colx şeklinde değer almaktadır
#worksheet.nrows dolu olan satır sayısı, ncols dolu olan sütun sayısını verir
from netmiko import ConnectHandler
import xlrd
workbook =xlrd.open_workbook("ssh_table.xlsx")
worksheet=workbook.sheet_by_name("connection_sheet")
row_value=worksheet.nrows
col_value=worksheet.ncols
deviceInfo =[]


for x in range (1,row_value):
    for y in range (col_value):
         deviceInfo.append(worksheet.cell_value(x,y))
    deviceInfo[4]=int(deviceInfo[4])
    deviceConnection ={
        'device_type':str(deviceInfo[0]),
        'host':str(deviceInfo[1]),
        'username':str(deviceInfo[2]),
        'password':str(deviceInfo[3]),
        'port':deviceInfo[4],
        'secret':str(deviceInfo[5])
        }
    baglanti = ConnectHandler(**deviceConnection)
    print(baglanti.send_command("show run"))
    deviceInfo.clear()