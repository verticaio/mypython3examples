#!/bin/bash


echo -e "\e[1;31m --- Cleaning existing inventory file \e[0m"
echo "" > ./inventory.txt

echo -e "\e[1;31m --- Executing icinga_client_env.yml...  \e[0m"
ansible-playbook icinga_client_env.yml -i ./hosts

echo -e "\e[1;31m --- Executing icinga_server.yml...  \e[0m"
ansible-playbook  icinga_server.yml  -i ./hosts

echo -e "\e[1;31m --- Executing icinga_node_wizard.yml ...  \e[0m"
ansible-playbook icinga_node_wizard.yml -i  ./hosts

echo -e "\e[1;31m --- Signing client certificate on server node ...  \e[0m"
ansible-playbook icinga_server_sign_ca.yml -i  ./hosts

result=$(echo $?)
   if [ $result -eq '0' ];
   then
        echo " --- Icinga Client Successfuly installed all servers"
   else
        echo " --- Icinga Client error happen "
   fi
