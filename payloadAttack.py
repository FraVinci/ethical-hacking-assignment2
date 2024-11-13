from scapy.all import IP, TCP, send

ip_layer = IP(dst="192.168.56.102")  #IP address of the victim's machine
tcp_layer = TCP(dport=80, sport=12345, flags="S")  #HTTP port and flag SYN

#HTTP GET with personalized payload
http_payload = (
    "GET /index.html HTTP/1.1\r\n"
    "Host: 192.168.56.102\r\n"
    "User-Agent: ScapyTest/1.0\r\n"
    "Accept: */*\r\n"
    "Custom-Payload: This is a playload that may contain malicious code\r\n"
    "\r\n"
)

packet = ip_layer / tcp_layer / http_payload

send(packet)
print("HTTP GET sendt with personalized payload\n")
print(http_payload)
