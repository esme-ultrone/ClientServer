# Client Server example

Here is a sample of and client/server architecture.
The server is make in Python and client in C.

The goal of this sample is just to demonstrate the general architecture so there are no fancy actions performed. The client send a message (string format) to the server that send him back the uppercase version of the input. That's all. 

###Here are the step to launch all the process :

- First, launch the server. It will run and wait for incomming connection from clients.
```sh
python3 main.py
```

- To launch the client, first you have to compile it through the makefile since it C program. Then run the "app" created.

```sh
make clean #Just in case
make
./app
```