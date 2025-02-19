# TCP SYN Port Scanner

This script uses [Scapy](https://scapy.net/) to perform a TCP SYN scan on a specified target and a list of ports. It sends a SYN packet to each port and analyzes the response to determine if the port is open, closed, or filtered.

## Features

- **TCP SYN Scan:** Sends a SYN packet and analyzes the response:
  - **Open Port:** Responds with a SYN-ACK packet.
  - **Closed Port:** Responds with a RST-ACK packet.
  - **Filtered Port:** No response received.
- **RST Packet:** If a port is open, a RST packet is sent to gracefully close the connection.

## Prerequisites

- **Python 3.x:** Make sure Python 3 is installed.
- **Scapy:** Install Scapy using pip:
  ```bash
  pip install scapy

## Usage

1. **Modify Target and Ports:**
   - Open the script file and change the `target` variable to the IP address of the host you want to scan.
   - Update the `ports` list with the desired ports to scan.

2. **Run the Script:**
   ```bash
   sudo python3 tcp_syn_scanner.py
   ```
   Replace `main.py` with the name of your script file.

3. **Interpreting Results:**
   - **Open:** The port is accepting connections.
   - **Closed:** The port is not accepting connections.
   - **Filtered:** No response was received, possibly due to firewall rules or network filtering.

## How It Works

1. **Packet Creation:**
   - The script constructs a TCP packet with the SYN flag set using `TCP(dport=port, flags="S")` and sends it to the target IP.
2. **Response Analysis:**
   - If no response is received within the specified timeout, the port is considered **Filtered**.
   - If a TCP packet with a SYN-ACK flag (`0x12`) is received, the port is **Open**.
   - If a TCP packet with a RST-ACK flag (`0x14`) is received, the port is **Closed**.
3. **Connection Teardown:**
   - For open ports, a TCP RST packet is sent to reset the connection.

## Disclaimer

- This script is intended for educational purposes and authorized security testing only.
- **Do not use this script on networks or hosts without explicit permission.** Unauthorized scanning can be illegal and unethical.


