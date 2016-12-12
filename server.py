import socket,sys
import re

host = ''
port = 12345

# AF_INET 跟外網 ipv4 tcp udp || AF_UNIX 內部溝通
# SOCK_STREAM TCP || SOCK_DGRAM UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", port))
sock.listen(3)
sock.settimeout(10)
(csock, adr) = sock.accept()
print("Client Info: ", csock , adr)
while True:
	msg = csock.recv(1024)
	print("Client send: " + msg.decode("utf=8"))
	mmm = input("To Client: ")
	if(re.search(r"^exit$",mmm) != None):
		break
	csock.send(mmm.encode("utf=8"))
csock.close()