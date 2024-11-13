from scapy.all import *
import random
import time

def slow_port_scan(target_ip, ports):
  
    print(f"Start slow port scan on {target_ip}...\n")
    
    #Mixing the order of ports to avoid sequential scanning
    random.shuffle(ports)

    for port in ports:

        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        
        #Send the package and wait for a reply
        response = sr1(packet, timeout=1, verbose=0)
        
        if response is not None:
            if response.haslayer(TCP) and response[TCP].flags == 0x12:
                print(f"Porta {port} open")
                #Send the RST packet to close the connection
                sr(IP(dst=target_ip) / TCP(dport=port, flags="R"), timeout=1, verbose=0)
            elif response.haslayer(TCP) and response[TCP].flags == 0x14:
                print(f"Porta {port} closed")
            elif response.haslayer(ICMP):
                print(f"Filtered {port} port (received ICMP packet)")
        else:
            print(f"Port {port} no response")
        
        #Random delay between requests to avoid detection
        delay = random.uniform(1, 30)
        time.sleep(delay)

    print("\nScan completed")

#IP address of the victim's machine
target_ip = "192.168.56.102" 

ports = list(range(20, 30))  #List of scanning ports
slow_port_scan(target_ip, ports)
