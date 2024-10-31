import socket
import threading

# Setup TCP and UDP sockets
s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to port 7000 for both protocols
s_tcp.bind(('', 7000))
s_udp.bind(('', 7000))

# Start listening for TCP connections
s_tcp.listen(5)

print("Server is running on port 7000, waiting for connections...")

# TCP handler function
def tcp_handler():
    while True:
        conn, addr = s_tcp.accept()
        print(f"TCP connection accepted from {addr}")
        data = conn.recv(1024)
        print(f"Received TCP data: {data.decode()}")
        conn.send(data)
        print(f"Sent TCP echo back to {addr}")
        conn.close()
        print(f"TCP connection with {addr} closed")

# UDP handler function
def udp_handler():
    while True:
        data, addr = s_udp.recvfrom(1024)
        print(f"Received UDP data from {addr}: {data.decode()}")
        s_udp.sendto(data, addr)
        print(f"Sent UDP echo back to {addr}")

# Start TCP and UDP handlers
threading.Thread(target=tcp_handler).start()
threading.Thread(target=udp_handler).start()
