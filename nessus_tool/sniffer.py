from scapy.all import sniff, wrpcap

packets = []

def capture_packet(packet):
    packets.append(packet)

def start_sniffing():
    sniff(prn=capture_packet, count=20)

def save_pcap(filename="capture.pcap"):
    wrpcap(filename, packets)
