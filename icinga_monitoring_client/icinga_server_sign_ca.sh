#!/bin/bash
ca_list=$(icinga2  ca list | awk -F'|' '{ print $1}' | grep -iE -v -e '*' -e 'Fingerprint' -e '-----------------------------------------------------------------')
for i in $ca_list;
do
    icinga2 ca sign $i
done
