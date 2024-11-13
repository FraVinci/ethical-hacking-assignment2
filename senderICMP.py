from scapy.all import *

def send_covert_message(target_ip, covert_message):
    message_bytes = covert_message.encode()
    
    for byte in message_bytes:
        #Creation of ICMP packet
        packet = IP(dst=target_ip)/ICMP(type=8)/Raw(load=bytes([byte]))
        
        # Invio del pacchetto
        send(packet, verbose=False)
        print(f"Inviato byte: {byte} ({chr(byte)})")

if __name__ == "__main__":
    target_ip = "192.168.56.102"  #IP address of the victim's machine
    covert_message = "Example_of_ICMP_covert_channel"
    
    send_covert_message(target_ip, covert_message)
