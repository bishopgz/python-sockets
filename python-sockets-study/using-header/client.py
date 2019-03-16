import socket

HEADER_LIMIT = 10

# define socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # streaming 
s.connect((socket.gethostname(), 8888))



while True:
	full_msg = ''
	new_msg = True
	while True:
		msg = s.recv(16) # 8 bytes is the size of a chunk of data
		if new_msg:
			print("new msg len:",msg[:HEADER_LIMIT])
			msg_len = int(msg[:HEADER_LIMIT])
			new_msg = False
		
		# append to original full msg
		full_msg += msg.decode('utf-8')
		# if full msg is within the limit of the expeced length 
		if len(full_msg)-HEADER_LIMIT == msg_len:
			print('Full message received.')
			print(full_msg)
			# reset properties
			new_msg = True
			full_msg = ''