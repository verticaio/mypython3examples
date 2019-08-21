## IBM Integration Bus services export script for any Inventory system
problem is that we  have IBM integration Bus and you know there is much   service url list and command line options(mqsireportproperties) didn't give you appropriate information but you can get all information from iib node api in which i did below variant.
Script is connected to remote servers for  taking hostname and  all running node urls with ansible( may more nodes inside of server). After that these arguments is passed to python script then python script connect every node api then parse  nodename, executing groups, service name and at the end rest and wsdl services from web xml and show you as csv format
```
For using: Clone project , change directory and execute as below
$ ansible-playbook iibdev.yaml

In result report.txt file will be generated and content will be as below:
servername,nodename,execution_name,servicename,serviceurl
server.intern.local , TESTNODE1 , ServerA , information , http://localhost:7824/information/v1
server.intern.local , TESTNODE2 , ServerA , helper , http://server.intern.local:7802/helper?wsdl
server.intern.local , TESTNODE3 , ServerA , service_url3 , http://server.intern.local:1111/service_url3?wsdl
server2.intern.local , TESTNODE4 , ServerA , service_url1 , http://server.intern.local:2222/service_url1?wsdl
server2.intern.local , TESTNODE5 , ServerA , service_url2 , http://server.intern.local:3333/service_url2?wsdl

```

### Future feature:
Next converted this csv is converted to Excel format and pushed to inventory system with rest API