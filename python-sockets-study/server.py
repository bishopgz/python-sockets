import socket

# define socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # streaming  
s.bind((socket.gethostname(), 8888))
s.listen(5); # queue of 5

# listen for connections
while True:
	client_socket, address = s.accept()
	print("Connection from {address} has been made!")
	client_socket.send(bytes("Hey client!", "utf-8")) # send info to it
