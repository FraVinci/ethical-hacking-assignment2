import time
import random
from scapy.all import *

#IP address of the victim's machine
destIp = "192.168.56.102"
#Port to scan, random order
portsToScan = list(range(20, 1024))
random.shuffle(portsToScan)

def fragmentedSlowScan(destIp, portsToScan, minDelay=60, maxDelay=300):
    for port in portsToScan:
        #SYN packet with random ID
        pkt = IP(dst=destIp, ttl=random.randint(64, 128), id=random.randint(1000, 50000), flags="MF") / TCP(dport=port, flags="S")

        #First packet fragment
        send(pkt, verbose=0)
        
        #Random delay
        delay = random.uniform(minDelay, maxDelay)
        print(f"Fragment packet sent to port {port}\nNext scan: {delay/60:.2f} minutes\n-------------")
        
        time.sleep(delay)

print(f"start slow port scan on {destIp}...\n")
fragmentedSlowScan(destIp, portsToScan)
