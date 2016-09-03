# import socket,sys
# def connection( port ):
# 	global s
# 	try:
# 	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	except socket.error:
# 	    print 'Failed to create socket'
# 	    sys.exit()
# 	print '[+] Listening for connections on port '+str(port)+'.'
# 	s.bind(('127.0.0.1',port))
# 	print "Waiting for connection"
# 	s.listen(5)
# 	global addr
# 	c,addr=s.accept()
# 	print 'Got connection from',addr
# 	c.send("Welcome")
# 	return c

# def server( c ):
# 	while 1:
# 		data = c.recv(512)
# 		if data == 'bye':
# 			print addr[0], data
# 			c.close()
# 			return True;
# 		else:
# 			print addr[0], data
# 		message = raw_input ( ">>" )
# 		c.send(message)
# def loop( port ):
	
# 	c = connection(port)
# 	server_connection = server(c)
# 	if server_connection == True:
# 		loop( port )

# port=12344
# loop(port)
import socket,sys
from thread import *
	
def intialise( port ):
	try:
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error:
	    print 'Failed to create socket'
	    sys.exit()
	print '[+] Listening for connections on port '+str(port)+'.'
	s.bind(('127.0.0.1',port))
	print "Waiting for connection"
	return s
def thread( s ):
	s.listen(5)
	global addr
	c,addr = s.accept()
	print 'Got connection from',addr
	c.send("Welcome")
	start_new_thread(clientthread ,(c,))

def clientthread( c ):
	while 1:
		data = c.recv(512)
		if data == 'bye':
			print addr[0], data
			c.close()
			return True;
		else:
			print addr[0], data
		message = raw_input ( ">>" )
		c.send(message)

def run( port ):
	socket = intialise(port)
	while  True:
		thread(socket)

port=12345
run(port)

	

