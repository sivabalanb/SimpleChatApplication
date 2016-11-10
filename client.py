#Sivabalan Balasubramanian
#UDP Client
import sys
from socket import * 
serverName = '127.0.0.1' 
serverPort = 12048 
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.bind(('', 5049)) 

message1 = raw_input('Client A:')
if message1=="exit":
    clientSocket.close()
    sys.exit()
else:
    clientSocket.sendto(message1,(serverName, serverPort))
while True:
	modifiedMessage, serverAddress =clientSocket.recvfrom(2048)
	if modifiedMessage=="EXIT":
	    print "Bye..I am leaving"
	    clientSocket.close()
	    #sys.exit()
	print "Client B: %s" %modifiedMessage
	message = raw_input('Client A:')
	
	if message.upper()=="EXIT":
	    clientSocket.sendto(message,(serverName, serverPort))
	    clientSocket.close()
	    break;
	else:	
	    clientSocket.sendto(message,(serverName, serverPort)) 
