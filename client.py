import socket


mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("localhost", 9001))

request = "GET http://localhost HTTP/1.0\r\n\r\n".encode()

mysocket.send(request)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysocket.close()
