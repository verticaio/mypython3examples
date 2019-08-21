### Rule for executing this script.
```
Prepare your hosts file and execute main.sh file as below
bash main.sh

main.sh steps
1. icinga_client_env.yml must be executed  all client servers(For checking network and internet access, configure redhat subscriber and  installing packages,  write remote host ip and name to inventory file  in which located ansible server)
2. after executed first step succesfully then icinga_server.yml  executed icinga_server_config.sh on icinga server  and write ticket number  to inventory file  in which ansible copy that file to icinga server and copy from icinga server to ansible server
3. icinga_node_wizard.yml executed icinga_node_wizard.sh together  inventory file on all client nodes
4. last step signing client certiticates with icinga_server_sign_ca.sh  on icinga server
```