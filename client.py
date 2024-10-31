import socket

server_ip = '141.148.223.177'  # Replace with your server's IP
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
