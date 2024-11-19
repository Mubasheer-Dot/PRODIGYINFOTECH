from scapy.all import sniff

# Callback function to process each packet
def analyze_packet(packet):
    try:
        # Extract basic information
        source_ip = packet[0][1].src
        destination_ip = packet[0][1].dst
        protocol = packet[0][1].proto
        
        # Print extracted information
        print(f"Source IP: {source_ip}, Destination IP: {destination_ip}, Protocol: {protocol}")
        
        # Display payload if available
        if packet.haslayer('Raw'):
            print(f"Payload: {bytes(packet['Raw']).decode('utf-8', errors='ignore')}")
    except Exception as e:
        print(f"Error processing packet: {e}")

# Main function to capture packets
def start_sniffer(interface=None, count=10):
    print("Starting packet capture...")
    sniff(iface=interface, prn=analyze_packet, count=count)
    print("Packet capture complete.")

# Run the sniffer
if _name_ == "_main_":
    # You can specify an interface (e.g., "eth0") or leave it as None to capture on the default interface
    start_sniffer(interface=None, count=5)