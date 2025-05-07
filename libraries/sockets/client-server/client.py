import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 9090)
client_socket.connect(server_address)
try:
    # Send data to the server
    message = "Hello from client!"
    print(f"Sending: {message}")
    client_socket.send(message.encode('utf-8'))

    # Look for the response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received: {response}")
finally:
    # Close the socket to clean up
    client_socket.close()
