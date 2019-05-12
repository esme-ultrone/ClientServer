from serverClass import CustomServer

if __name__ == "__main__":
	
	try:
		myServer = CustomServer('localhost', 12345)
		myServer.listen(1)
		myServer.launch()
		
	except KeyboardInterrupt:
		del myServer