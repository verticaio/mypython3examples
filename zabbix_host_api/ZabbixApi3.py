from pyzabbix import ZabbixAPI
from pprint import pprint

zapi = ZabbixAPI("http://192.168.1.1/zabbix/")
zapi.login("Admin", "admin")
print("Connected to Zabbix API Version %s" % zapi.api_version())

# for h in zapi.host.get(output="extend"):
#   pprint(h)


hosts = zapi.host.get(output=["available", "name", "host", "status"])
# print(hosts)


#print("Show Active Hosts:")
#a = 0
#for host in hosts:
#    if host.get('available') == '1':
#       print('-------------------')
#        print(host.get('name'))
#        print(host.get('host'))
#       a = a+1
#print("Active hostlarin cemi:", a)


print("Show Disabled Hosts:")
for host in hosts:
    if host.get('available') == '0':
        print('-------------------')
        print(host.get('name'))
        print(host.get('host'))

print("Show Failed Hosts:")
for host in hosts:
    if host.get('available') == '2':
        print('-------------------')
        print(host.get('name'))
        print(host.get('host'))