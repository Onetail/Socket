import socket
import re

host = "127.0.0.1"
port = 12345

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_address = (host,port)
print ("Connecting to %s port %s" % server_address)
sock.connect(server_address)


message =""
while True:
	message = input("To Server: ")
	if(re.search(r"^exit$",message) != None):
		break
	sock.send(message.encode("utf=8"))
	data = sock.recv(1024)
	print("接收 : " + data.decode("utf=8"))
print("Closing connection to the server")
sock.close()