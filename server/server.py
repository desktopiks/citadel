import socket, time

HOST = socket.gethostbyname(socket.gethostname()) #127.0.1.1
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
clients = []  

def start_server():
    print(f"[ Server Started ] Server is listening on {HOST}:{PORT}")
    quit = False
    while not quit:
        try:
            data, addr = server.recvfrom(1024)

            if addr not in clients:
                clients.append(addr)
            
            itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

            print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
            print(data.decode("utf-8"))

            for client in clients:
                if addr != client:
                    server.sendto(data, client)
        except:	
            print("\n[ Server Stopped ]")
            quit = True
    server.close()

start_server()
