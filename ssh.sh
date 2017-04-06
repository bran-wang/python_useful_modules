#!/bin/bash

# ssh-keygen -t rsa
# cp id_rsa.pub to remote host renamed ~/.ssh/authorized_keys

echo ""
echo "which host would you like to ssh ?"
echo "----------------------------------------------"
echo "1) esxi_ubuntu: 10.117.170.206"
echo "2) vdnet_ubuntu: 10.160.134.103"
echo "----------------------------------------------"

echo ""
read -n1 -p "please enter host number (like: 1) : " host_num
echo ""
echo "----------------------------------------------"
case $host_num in
    1)
        echo "ssh to esxi_ubuntu"
        ssh wyp@10.117.170.206 -p 22;;
    2)
        echo "ssh to vdnet_ubuntu"
        ssh root@10.160.134.103 -p 22;;
    *)
        echo "error choice";;
esac
