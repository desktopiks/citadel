import socket, threading, time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 0

server = ("127.0.1.1", 5050) #Change if server host is different.

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((HOST, PORT))
client.setblocking(0)

def receving(name, sock):
	key = 8194
	shutdown = False
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				decrypt = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
				time.sleep(0.2)
		except:
			pass

def start_client():
	key = 8194
	shutdown = False
	join = False
	alias = input("Name: ")
	rT = threading.Thread(target=receving, args=("RecvThread", client))
	rT.start()

	while shutdown == False:
		if join == False:
			client.sendto(("["+alias + "] => join chat ").encode("utf-8"), server)
			join = True
		else:
			try:
				message = input()
				crypt = ""
				for i in message:
					crypt += chr(ord(i)^key)
				message = crypt
				if message != "":
					client.sendto(("["+alias + "] :: "+message).encode("utf-8"),server)
				time.sleep(0.2)
			except:
				client.sendto(("["+alias + "] <= left chat ").encode("utf-8"),server)
				shutdown = True

	rT.join()
	client.close()

start_client()