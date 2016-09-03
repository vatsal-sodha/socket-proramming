import socket
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
    data = data[7:]
    data = data.replace('$' , '')
    data = data.replace('0111110','')
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
            message  = bitstuffing(message)
            client_socket.send(message)
            print message
            
