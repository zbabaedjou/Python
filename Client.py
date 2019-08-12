import socket

server_ip = "192.168.1.4"
server_port = 8090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

request = "hiiiiiiiiiiiii"
client.send(request.encode('utf-8'))
response = client.recv(4096)

print(response)
