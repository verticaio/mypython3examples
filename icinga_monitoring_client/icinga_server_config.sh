#!/bin/bash

### icinga general host file for monitoring objects
icinga_conf="/etc/icinga2/objects.d/master/hosts.conf"
### operating system hosts file for icing knowing clients
system_conf="/etc/hosts"
###  general zone config file for clients
zone_conf="/etc/icinga2/zones.conf"
### For reading ip,hostname and writing ticket to this file based on every hostname
inven_conf="inventory.txt"
### resutl log file for every client
log_file="icinga_server_config.log"

### backup important config files before script started
cp $icinga_conf /etc/icinga2/objects.d/master/hosts.conf_$(date +%Y_%M_%d_%H_%M_%S)
cp $system_conf  /etc/hosts_$(date +%Y_%M_%d_%H_%M_%S)
cp $zone_conf  /etc/icinga2/zones.conf_$(date +%Y_%M_%d_%H_%M_%S)
cp $inven_conf inventory.txt_$(date +%Y_%M_%d_%H_%M_%S)

echo -e "   ---- Icinga Server COnfig Sh Started  ---- "   >> $log_file

add_conf(){
        os_ip=$1
        os_hostname=$2
echo -e " --- Icinga server script started for $os_hostname"   >> $log_file
echo " --- Add icinga host file for monitoring" >> $log_file
        echo -e "object Host \""$os_hostname"\" {
  check_command = \"hostalive\"
  address = \""$os_ip"\"
  vars.client_endpoint = name
  vars.procs_warning = 550
  vars.procs_critical = 650
  vars.procs_argument = \"pmon\"
  vars.procs_warning = 1
  vars.procs_critical = 1
  vars.disk_partitions_excluded = [ \"/bckp\", \"/run/user/1000/gvfs\", \"/run/user/0/gvfs\", \"/media\" ]
  vars.disk_excluede_type = [ \"fuse.gvfsd-fuse\", \"fuse.gvfs-fuse-daemon\" ]
  vars.notification[\"mail\"] = {
    groups = [ \"processing\" ]
  }
}" >> $icinga_conf

echo -e "\n" >> $icinga_conf

echo " --- Add etc host file"  >> $log_file
echo -e "$os_ip\t$os_hostname" >> $system_conf

echo " --- Add zone file for endpoint, find endpoint line number and insert endpoint string  after three line" >> $log_file
endpoint_line_num=$(cat $zone_conf  | grep -n -iE -w Endpoint | tail -1 | cut -d: -f1)
new_end_line_nub="$(($endpoint_line_num+4))"
sed -i "$new_end_line_nub i\\object Endpoint \"$os_hostname\" \{  \\n   host = \"$os_ip\" \/\/the master actively tries to connect to the client  \\n\} \\n "  $zone_conf

echo " --- Add zone file for zone" >> $log_file
zone_line_num=$(cat $zone_conf  | grep -n -iE -w endpoints  | tail -1 | cut -d: -f1)
new_zone_line_nub="$(($zone_line_num+5))"
sed -i  "$new_zone_line_nub i\\object Zone \"$os_hostname\" \{ \\n endpoints = \[ \"$os_hostname\" \] \\n \\n parent = \"master\"  \\n\} \\n "  $zone_conf

echo " --- Generate Ticket and add to variable then add to specific after host" >> $log_file
ticket=$(icinga2 pki ticket --cn $os_hostname  --salt 123456)

echo " --- Add client ticket to  inventory file for retriving icinga client node wizard setup" >> $log_file
sed -i "/$os_hostname/s/$/\,$ticket/"  $inven_conf

echo " --- Check Icinga Config" >> $log_file
output=$(icinga2 daemon -C)
icinga2 daemon -C
result=$(echo $?)
   if [ $result -eq '0' ];
   then
        echo " --- This Client $os_hostname  config successfully " >> $log_file
   else
        echo -e "\n" >>  $log_file
        echo -e "$output" >> $log_file
        echo -e "\n" >>  $log_file
        echo " --- Happent client  $os_hostname  config error " >>  $log_file
   fi

echo -e "\n" >>  $log_file

}

while read line
    do
        os_ip=$(echo $line  | awk -F',' '{ print $1}')
        os_hostname=$(echo $line  | awk -F',' '{ print $2}')
        add_conf $os_ip $os_hostname
    done < $inven_conf
