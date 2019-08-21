#!/bin/bash

node_wizard(){
icinga_host_name="icinga.intern.local"
icinga_ip_addr="192.168.1.2"
client_hostname=$1
ticket_num=$2
/usr/bin/expect<<EOF
    spawn icinga2 node wizard
    expect "n]:"           {send "Y\r"}
    expect "]:"            {send "$client_hostname\r"}
    expect "node):"        {send "$icinga_host_name\r"}
    expect "n]:"           {send "Y\r"}
    expect "FQDN):"        {send "$icinga_ip_addr\r"}
    expect "]:"            {send "5665\r"}
    expect "N]:"           {send "N\r"}
    expect "N]:"           {send "y\r"}
    expect "):"            {send "$ticket_num\r"}
    expect "[]:"           {send "0.0.0.0\r"}
    expect "[]:"           {send "5665\r"}
    expect "N]:"           {send "y\r"}
    expect "N]:"           {send "y\r"}
    expect "]:"            {send "$client_hostname\r"}
    expect "]:"            {send "master\r"}
    expect "N]:"           {send "N\r"}
    expect "n]:"           {send "Y\r"}
    expect eof
EOF
}

ticket_num=$(cat inventory.txt |  awk -v hostname=$(hostname) -F',' '$2 ~ hostname  { print $3}')
node_wizard $(hostname) $ticket_num
