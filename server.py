#Sivabalan Balasubramanian
#UDP Server

from socket import *
serverPort = 12048
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(('', serverPort))
print 'The server is ready to receive'
while True: 
	message,clientAddress = serverSocket.recvfrom(2048) 
	modifiedMessage = message.upper() 
	clientAddress=('',5048)
	if modifiedMessage=='EXIT':
	    serverSocket.sendto("Bye...I am leaving",clientAddress)
	    print "Closing the Connection by client A"
	    break; 
	else:
	    serverSocket.sendto(modifiedMessage, clientAddress)
	#Where Client B responds to the message
	    message1,clientB = serverSocket.recvfrom(2048)
	    modifiedMessage1 = message1.upper()
	    clientB=('',5049)
	    if modifiedMessage1=='EXIT':
		serverSocket.sendto("Bye...I am leaving", clientB)
		print "Closing the Connection by client B"
	    else:
	    	serverSocket.sendto(modifiedMessage1, clientB)
