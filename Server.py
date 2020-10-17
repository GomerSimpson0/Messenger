import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9090))
client = []

print('Server started')

while True:
	data, add = sock.recvfrom(1024)
	print(add[0], data.decode('utf-8'))
	if add not in client:
		client.append(add)
	for clients in client:
		if clients == add:
			continue
		sock.sendto(data, clients)