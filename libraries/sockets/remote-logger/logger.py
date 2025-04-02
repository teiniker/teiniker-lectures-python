import socket
from datetime import datetime

# Define the log file name
LOG_FILE = 'server_log.txt'

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a local address and a port
server_address = ('localhost', 8080)
server_socket.bind(server_address)
# Listen for incoming connections (backlog of 5 connections)
server_socket.listen(5)
print(f"Server listening on {server_address[0]}:{server_address[1]}...")

def log_message(message:str) -> None:
    """Log the message with a timestamp."""
    with open(LOG_FILE, 'a', encoding='utf-8') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"[{timestamp}] {message}\n")

while True:
    client_socket, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            # Print and log the received data
            print(f"Received: {data}")
            log_message(f"{client_address}: {data}")

            # Respond to the client
            client_socket.send("OK".encode('utf-8'))
    finally:
        client_socket.close()
