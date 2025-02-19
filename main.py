# from scapy.all import IP,TCP, sr1


# target_ip = '8.8.8.8'
# target_port = 80

# syn_packet = IP(dst=target_ip)/TCP(dport=target_port,flags='S')
# response = sr1(syn_packet,timeout=2)


# response.show() if response else print('No response')


# from scapy.all import IP, TCP, sr1,UDP

# # Define the target IP and port
# target_ip = "8.8.8.8"  # Replace with your target IP
# target_port = 80       # Replace with the port you want to target

# # Build the SYN packet (TCP flag 'S' indicates SYN)
# syn_packet = IP(dst=target_ip) / UDP(dport=target_port)

# # Send the packet and wait for a response (with a timeout of 2 seconds)
# response = sr1(syn_packet, timeout=2)

# # Display the response if received
# if response:
#     response.summary()
# else:
#     print("No response")


# from scapy.all import IP, UDP, ICMP, sr1

# # Define the target IP and port
# target_ip = "8.8.8.8"  # Replace with your target IP
# target_port = 80       # Replace with the port you want to target

# # Build the UDP packet
# udp_packet = IP(dst=target_ip) / UDP(dport=target_port)

# # Send the packet and wait for a response (with a timeout of 2 seconds)
# response = sr1(udp_packet, timeout=2)

# # Check for ICMP Port Unreachable message
# if response:
#     if response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code == 3:
#         print(f"Port {target_port} is closed (ICMP Port Unreachable received).")
#     else:
#         print(f"Port {target_port} might be open or filtered (no ICMP error received).")
# else:
#     print(f"No response received. Port {target_port} might be open or filtered.")



# from scapy.all import IP, Ether, sr1,ARP,srp


# response = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.10.0/23"))


# response.summary() if response else print('no response')




from scapy.all import IP, TCP, sr1, send
import sys

# Target and ports to scan
target = "192.168.10.75"  # Change to your target IP
ports = [22, 80, 443, 8080]  # List of ports to scan

# Perform TCP SYN scan
for port in ports:
    packet = IP(dst=target)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)

    if response is None:
        print(f"Port {port}: Filtered (No response)")
    elif response.haslayer(TCP):
        if response[TCP].flags == 0x12:  # SYN-ACK
            print(f"Port {port}: Open")
            send(IP(dst=target)/TCP(dport=port, flags="R"), verbose=0)  # Send RST to close
        elif response[TCP].flags == 0x14:  # RST-ACK
            print(f"Port {port}: Closed")
    else:
        print(f"Port {port}: Unknown state")






