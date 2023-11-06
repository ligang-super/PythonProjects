# -*- coding:utf-8 -*-
# __author__='ligang'

from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP
#from one_ping import scanpy_ping_on

def scapy_tcp_scan(hostname, lport, hport):

    packet = IP(dst=hostname)/TCP(dport=(int(lport), int(hport)), flags=2)
    result_ral = sr(packet, timeout=10, verbose=False)

from scapy.all import *

def is_port_open(ip, port):
    packet = IP(dst=ip)/TCP(dport=port, flags='S')
    response = sr(packet, timeout=1, verbose=False)[0]
    if response.haslayer(TCP) and response[TCP].flags == 0x12:
        return True
    else:
        return False

if __name__ == '__main__':
    print("Hello", os.path.basename(__file__))

    print(is_port_open("192.168.44.129", 8088))





