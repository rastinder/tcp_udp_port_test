Here’s the updated README with the firewall command included:

---

# 🖥️ TCP and UDP Echo Server in Python

This project provides a simple **TCP and UDP echo server** built with Python. The server listens on port `7000` and echoes back any data sent to it, supporting both TCP and UDP protocols. It's lightweight, multi-threaded, and comes with detailed logging for easy debugging.

## 🌟 Features
- **🌐 Dual Protocol Support**: Listens for both TCP and UDP traffic on port `7000`.
- **🧵 Multi-threaded**: Runs TCP and UDP communication concurrently on separate threads.
- **🔍 Debugging Output**: Logs all connections, data received, and responses sent, providing insight into server activity.
  
## 🚀 Quick Start

Run the following one-liner to create and start `ping.py` with the TCP/UDP echo server:

```bash
echo -e "import socket, threading\ns_tcp, s_udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\ns_tcp.bind(('', 7000)), s_udp.bind(('', 7000)), s_tcp.listen(5)\nprint('Server running on port 7000...')\ndef tcp_handler():\n while True: conn, addr = s_tcp.accept(); print(f'TCP from {addr}'); data = conn.recv(1024); print(f'TCP recv: {data.decode()}'); conn.send(data); conn.close(); print(f'TCP echo sent to {addr}')\ndef udp_handler():\n while True: data, addr = s_udp.recvfrom(1024); print(f'UDP from {addr}: {data.decode()}'); s_udp.sendto(data, addr); print(f'UDP echo sent to {addr}')\nthreading.Thread(target=tcp_handler).start(), threading.Thread(target=udp_handler).start()" > ping.py && python3 ping.py
```

This command will:
1. Create a `ping.py` file with the echo server code.
2. Start the server, listening on **both TCP and UDP** protocols on port `7000`.

## 🔧 Disable Firewall (if needed)

If your firewall is preventing access, use this command to temporarily disable it:

```bash
sudo cp /etc/iptables/rules.v4 /etc/iptables/rules.v4.bak && sudo truncate -s 0 /etc/iptables/rules.v4
```

This command backs up your current firewall rules and clears them. **Be cautious**, as this will disable all firewall protection on the server. Make sure to re-enable it when you’re done testing.

## 🧑‍💻 Testing the Server

To test the echo server, use the following `client.py` script on your **client machine**:

```python
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
```

This script:
- **Sends** a "Hello" message over **TCP** and **UDP** to the server on port `7000`.
- **Prints** the server's response to verify the echo functionality.

## 📝 Notes
- Ensure **port `7000`** is open on your server’s firewall and configured to allow both TCP and UDP traffic.
- The server will log all connections and data to assist with real-time debugging.

---

### 🛠️ Troubleshooting
If you encounter issues:
- **Check Network**: Verify your server’s firewall and security group settings allow incoming connections on port `7000`.
- **Confirm IP**: Ensure the `server_ip` variable in `client.py` is correctly set to your server’s IP.

Happy coding! 🎉
