TCP and UDP Echo Server in Python
This repository contains a simple TCP and UDP echo server in Python. It listens on port 7000 and echoes back any data sent to it. The server supports both TCP and UDP protocols, running each on separate threads, and includes print statements for debugging.

Features
TCP Support: Listens for TCP connections on port 7000, echoes received data back to the client.
UDP Support: Listens for UDP messages on port 7000, echoes received data back to the client.
Multi-threaded: Uses threads to handle TCP and UDP communication concurrently.
Debugging Output: Prints debugging information, including connection details and data received/sent, for easy monitoring.
Setup
Run the following command to create and start ping.py with the TCP/UDP echo server:

bash
Copy code
echo -e "import socket, threading\ns_tcp, s_udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\ns_tcp.bind(('', 7000)), s_udp.bind(('', 7000)), s_tcp.listen(5)\nprint('Server running on port 7000...')\ndef tcp_handler():\n while True: conn, addr = s_tcp.accept(); print(f'TCP from {addr}'); data = conn.recv(1024); print(f'TCP recv: {data.decode()}'); conn.send(data); conn.close(); print(f'TCP echo sent to {addr}')\ndef udp_handler():\n while True: data, addr = s_udp.recvfrom(1024); print(f'UDP from {addr}: {data.decode()}'); s_udp.sendto(data, addr); print(f'UDP echo sent to {addr}')\nthreading.Thread(target=tcp_handler).start(), threading.Thread(target=udp_handler).start()" > ping.py && python3 ping.py
This command will:

Create a ping.py script with the echo server code.
Start the server, listening on both TCP and UDP on port 7000.
Usage
To test the server, you can use a compatible client.py script to send and receive messages over TCP and UDP:

python
Copy code
import socket

server_ip = '141.148.223.177'
port = 7000

# TCP echo test
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect((server_ip, port))
tcp_client.sendall(b'Hello TCP')
tcp_data = tcp_client.recv(1024)
print("TCP Response:", tcp_data.decode())
tcp_client.close()

# UDP echo test
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.sendto(b'Hello UDP', (server_ip, port))
udp_data, _ = udp_client.recvfrom(1024)
print("UDP Response:", udp_data.decode())
udp_client.close()
This client.py script connects to the server and sends a test message over both TCP and UDP, verifying the echo functionality.

Notes
Ensure that port 7000 is open on the server and firewall settings allow both TCP and UDP traffic on this port.
The server will print debugging information to help monitor connections and data.
