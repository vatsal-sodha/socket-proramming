import socket

port=raw_input("Enter port number: ")
port=int(port)
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
ip=raw_input("Enter IP address: ")
client_socket.connect((ip,port))
while 1:
    data = client_socket.recv(512)
    if ( data == 'bye' ):
        print client_socket.getsockname()[0] , data
        client_socket.close()
        break;
    else:
        print client_socket.getsockname()[0] , data
        message = raw_input ( "SEND( TYPE bye to Quit):" )
        if (message == 'bye'):
            client_socket.send(message)
            client_socket.close()
            break;
        else:
            client_socket.send(message)
            
            
