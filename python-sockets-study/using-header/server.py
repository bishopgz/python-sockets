import socket

HEADER_LIMIT = 10

def add_header(msg):
	length = len(msg)
	st_len = len(str(length))
	if st_len <= HEADER_LIMIT:
		chars = st_len + (HEADER_LIMIT - st_len)
	header = str((str(length)+chars*' '+msg))
	return header


# define socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # streaming  
s.bind((socket.gethostname(), 8888))
s.listen(5); # queue of 5

# listen for connections
while True:
	client_socket, address = s.accept()
	print("Connection from {address} has been made!")
	msg = "Welcome to the server"
	processed = add_header(msg)
	client_socket.send(bytes(processed, "utf-8")) # send info to it
