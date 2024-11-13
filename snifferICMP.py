from scapy.all import *

reconstructed_message = []

def process_packet(packet):
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:
        
        if packet.haslayer(Raw):    
            #Playload
            byte_payload = packet[Raw].load
            reconstructed_message.append(byte_payload.decode(errors='ignore'))
            print(f"Byte received: {byte_payload} ({byte_payload.decode(errors='ignore')})")

def start_sniffer():
    print("Sniffer start... Waiting for ICMP packets...")
    sniff(filter="icmp", prn=process_packet, store=0)

if __name__ == "__main__":
    try:
        start_sniffer()
    except KeyboardInterrupt:
        full_message = ''.join(reconstructed_message)
        print(f"\nMessage reconstructed: {full_message}")
