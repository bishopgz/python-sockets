import socket

# define socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # streaming 
s.connect((socket.gethostname(), 8888))

# buffer size chunk 
while True:
	msg = s.recv(8) # 8 bytes is the size of a chunk of data
	print(msg.decode("utf-8"))