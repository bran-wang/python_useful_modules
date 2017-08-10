__author__ = 'branw'

import ipaddr

mgmt_network_cidr = "192.168.111.1/24"
mgmt_ip_range_start = "192.168.111.1"
mgmt_ip_range_end = "192.168.111.110"
mgmt_network_gateway = "192.168.111.1"


ips = ipaddr.IPNetwork(mgmt_network_cidr)
print ips.ip
print ips.network
print ips.hostmask
print ips.netmask
print ips.prefixlen

print "-------------------\n"

ip_start = ipaddr.IPAddress(mgmt_ip_range_start)
ip_end = ipaddr.IPAddress(mgmt_ip_range_end)
print ips.Contains(ip_start)
print ips.Contains(ip_end)

gateway = ipaddr.IPAddress(mgmt_network_gateway)
print ips.Contains(gateway)

if gateway > ip_start or gateway < ip_end:
    print "gateway is in the ip pool, can not create network"