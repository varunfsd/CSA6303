
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

interface = input("Enter network interface: ")
count = int(input("Enter number of packets to capture: "))

print("\nStarting packet sniffing...\n")

sniff(iface=interface, prn=packet_callback,
      count=count, store=False)

print("\nPacket sniffing completed.")
