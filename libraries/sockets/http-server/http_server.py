import socket

# Configuration
HOST, PORT = 'localhost', 8080

# Read HTML content from file
def read_html(file_path):
    print(f"Reading HTML file: web/{file_path}")
    try:
        with open(f"web/{file_path}", 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "<html><body><h1>404 Not Found</h1></body></html>"

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"HTTP Server running on http://{HOST}:{PORT}/")

while True:
    client_socket, addr = server_socket.accept()
    try:
        request = client_socket.recv(1024).decode('utf-8')
        request_line = request.splitlines()[0]
        method, path, _ = request_line.split()

        print(f"Received {method} request for {path} from {addr}")

        if method == 'GET':
            html_content = read_html(path)
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                f"Content-Length: {len(html_content.encode('utf-8'))}\r\n"
                "Connection: close\r\n"
                "\r\n"
                f"{html_content}"
            )
        else:
            response = (
                "HTTP/1.1 405 Method Not Allowed\r\n"
                "Connection: close\r\n"
                "\r\n"
            )

        client_socket.sendall(response.encode('utf-8'))
    finally:
        client_socket.close()
