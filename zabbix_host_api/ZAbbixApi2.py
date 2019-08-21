import json
import urllib2

url = "http://192.168.1.1/zabbix/api_jsonrpc.php"
header = {"Content-Type": "application/json"}

# request json
data = json.dumps(
{
    "jsonrpc":"2.0",
    "method":"host.get",
    "params":{
        "output":["hostid","name"],
        "filter":{"host":""}
    },
    "auth":"8c67fd696eb3a6a877569b9bc34d6c22",
    "id":1,
})

# create request object
request = urllib2.Request(url, data)
for key in header:
    request.add_header(key, header[key])

# get host list
result = urllib2.urlopen(request)
response = json.loads(result.read())
result.close()
print("Number Of Hosts: ", len(response['result']))
for host in response['result']:
    print("Host ID:", host['hostid'], "Host Name:", host['name'])