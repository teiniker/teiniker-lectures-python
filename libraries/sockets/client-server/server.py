import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local address and a port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections (backlog of 1 connection)
server_socket.listen(1)
print(f"Server listening on {server_address[0]}:{server_address[1]}...")

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")

        # Receive the data in small chunks and retransmit it
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            print(f"Received: {data}")
            response = "Hello from server!"
            client_socket.send(response.encode('utf-8'))
    finally:
        # Clean up the connection
        client_socket.close()
