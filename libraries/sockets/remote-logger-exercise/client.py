import socket

server_address = ('localhost', 8080)

# List of test messages to send
test_messages = [
    "First log message",
    "Another log message",
    "Yet another message",
    "Final test message"
]

for message in test_messages:
    # Create a new socket for each message
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(server_address)

        # Send the message
        client_socket.send(message.encode('utf-8'))
        print(f"Sent: {message}")

        # Receive response from server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")
