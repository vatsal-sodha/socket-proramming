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
# import socket,sys 
# from thread import *
	
# def intialise( port ):
# 	try:
# 	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	except socket.error:
# 	    print 'Failed to create socket'
# 	    sys.exit()
# 	print '[+] Listening for connections on port '+str(port)+'.'
# 	s.bind(('127.0.0.1',port))
# 	print "Waiting for connection"
# 	return s
# def thread( s ):
# 	s.listen(5)
# 	global addr
# 	c,addr = s.accept()
# 	print 'Got connection from',addr
# 	c.send("Welcome")
# 	start_new_thread(clientthread ,(c,))
# 	message = raw_input ( ">>" )
# 	message1 = bitstuffing(message)
# 	c.send(message1)

# def clientthread( c ):
# 	while 1:
# 		data = c.recv(512)
# 		if data == 'bye':
# 			print addr[0], data
# 			c.close()
# 			return True;
# 		print addr[0], data


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
	message = bitstuffing("Welcome")
	c.send(message)
	start_new_thread(clientthread ,(c,))

def bitstuffing( message ):
	flag = '0111110'
	flag_content = '11111'
	if flag_content in message:
		count = 0
		index=0
		for char in message:
			if char == '1':
				count=count+1
			else:
				count = 0
			if count == 6:
				count = 0
				message = message[:index] + '$' + message[index:]
			index=index + 1
		bitstuffed_message = flag + message + flag
	else:
		bitstuffed_message = flag + message + flag	
			
	return bitstuffed_message
def run( port ):
	socket = intialise(port)
	while  True:
		thread(socket)
def clientthread( c ):
	while 1:
		data = c.recv(512)
		data = data[7:]
		data = data.replace('$' , '')
		data = data.replace('0111110','')
		if data == 'bye':
			print addr[0], data
			c.close()
			return True;
		else:
			print addr[0], data
		message = raw_input ( ">>" )
		message  = bitstuffing(message)
		c.send(message)
		print addr[0],message

def run( port ):
	socket = intialise(port)
	while  True:
		thread(socket)

port=12345
run(port)	

