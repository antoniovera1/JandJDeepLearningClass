import socket


print("Access http://localhost:9001")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(("localhost", 9001))
    server_socket.listen(5)

    while True:
        (clientsocket, address) = server_socket.accept()

        request = clientsocket.recv(5000).decode()
        print(request, end="~~~~~~~~~~~~~~~~~~~~~\n")

        response = "HTTP\1.1 200 OK\n"
        response += "Content-Type: text/html\n"
        response += "\n"
        response += "<html><body><h1>Hello world!</h1></body></html>\n"

        clientsocket.sendall(response.encode())
        clientsocket.shutdown(socket.SHUT_WR)
except KeyboardInterrupt:
    print("Shutting down...")

except Exception as e:
    print(e)

server_socket.close()
