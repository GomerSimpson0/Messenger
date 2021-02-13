import socket, time

port = 9090

clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('', port))

all_data = ''
quit = False
print("[ Server Started ]")

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

            itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        #all_data = all_data + data.decode('utf-8')

        #if 'join chat' in data.decode("utf-8"):
        #    s.sendto(all_data.encode("utf-8"), addr)

        for client in clients:
            if addr != client:
                s.sendto(data,client)
    except:
        print("\n[ Server Stopped ]")
        quit = True
s.close()
