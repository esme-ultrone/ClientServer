from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

class CustomServer:

	def __init__(self, addr = None, port = None): 
		# Set attribute following provided arguments.
		# If none, we use default value 
		self.addr = addr if addr != None else 'localhost' 
		self.port = port if addr != None else 10000

		# Create socket as TCP socket.
		self.sock = socket(AF_INET, SOCK_STREAM)
		# Bind the socket to the address and port we just configured.
		self.sock.bind((self.addr, self.port))

		print('Initiliaze server on the following address {}:{}.'.format(self.addr, self.port))

	def __del__(self):
		# We properly close the socket to avoid conflict when restarting the server
		self.sock.close()

	def listen(self, nbConnection = None):
		# Get number of maximum simultaneous connection to the server.
		# If none, set the value to 1 
		self.nbConnection = nbConnection if nbConnection != None else 1
		self.sock.listen(self.nbConnection) 	

	def launch(self):

		while True:
			# Wait for a client to send a message to the server
			clientSocket = self.waitForClientToConnect()

			try:
				# Get the data from client. Do stuff on it and send them back to the client
				data = self.getDataFromClient(clientSocket)
				data = self.doSomethingWithData(data)
				self.sendDataToClient(clientSocket, data)

			except KeyboardInterrupt:
				print('KeyboardInterrupt ... Stopping process.')
				self.sock.close()

	def waitForClientToConnect(self):
		# We have to return clientSocket to send him back data
		clientSocket, clientAddress = self.sock.accept()
		print('Connection received from {}'.format(clientAddress))
		return clientSocket
		

	def getDataFromClient(self, clientSocket):
		# 1024 is the size of the chunk read by the recv() method. 
		# Other value can fit too. 
		return clientSocket.recv(1024)

	def sendDataToClient(self, clientSocket, data):
		# We send back data to client and then closed the associated socket
		clientSocket.sendall(data)
		clientSocket.close()

	def doSomethingWithData(self, data):
		# Do some stuff with the data received from client
		return data.upper()
	