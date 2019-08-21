import xml.etree.ElementTree as ET
import urllib.request
import sys
import base64


# Argument list and variables
servername = sys.argv[1]
nodeurl = sys.argv[2]
URL = nodeurl + '/apiv1/executiongroups'

## You have with password or passwordless or  different password iibnode urls(it is management interface) and in my case I have two different password and passwordless url 
username = 'username'
password1 = 'pass1'
password2 = 'pass2'

# Check argument count
if len(sys.argv) is not 3:
    print("You have to execute script as following  python36 ./python_elementTree_URL.py server_hostname http://node_url:port")
    exit()

# Function for  Request URL(passwordless, and two different password)
def urlparse(url):
    try:
        file = urllib.request.urlopen(url)
        response = file.read()
        file.close()
        return ET.fromstring(response)
    except:
        try:
            req = urllib.request.Request(url)
            credentials = ('%s:%s' % (username, password1))
            encoded_credentials = base64.b64encode(credentials.encode('ascii'))
            req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
            file = urllib.request.urlopen(req)
            response = file.read()
            file.close()
            return ET.fromstring(response)
        except:
            req = urllib.request.Request(url)
            credentials = ('%s:%s' % (username, password2))
            encoded_credentials = base64.b64encode(credentials.encode('ascii'))
            req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
            file = urllib.request.urlopen(req)
            response = file.read()
            file.close()
            return ET.fromstring(response)

# Extract node name from node url that from coming ansible playbook as argument
nodename = urlparse(nodeurl + '/apiv1').attrib['name']

# Iterate  over all xml and parse
for exgr in urlparse(URL).getchildren():
    attributes = exgr.attrib
    if (attributes.get('runMode') == 'running'):
        executing_gn = attributes.get('name')
        # for soap services
        for wsdl_names in urlparse(URL + '/' + executing_gn + '/services').getchildren():
             attributes = wsdl_names.attrib
             service_name = attributes.get('name')
             # list services_url under WSDL
             for p in urlparse(URL + '/' + executing_gn + '/services/' + service_name + '/properties').findall('basicProperties'):
                 for i in p.getchildren():
                     if i.attrib['name'] == 'soapHTTPQueryURL':
                         print(servername,',', nodename,',', executing_gn,',',service_name,',',i.attrib['value'])
        # for restapis
        for rest_names in urlparse(URL + '/' + executing_gn + '/restapis').getchildren():
             attributes = rest_names.attrib
             service_name = attributes.get('name')
             for p in urlparse(URL + '/' + executing_gn + '/restapis/' + service_name + '/properties').findall('basicProperties'):
                 for i in p.getchildren():
                     if i.attrib['name'] == 'localBaseURL':
                         print(servername,',',nodename,',', executing_gn,',', service_name,',',i.attrib['value'])