# Problem Definition

the problem is implementation of a client-server application that follows the next algorithm:
1.	Server keeps ports 8000 and 8001 open.
2.	Each client generates a unique identifier for itself.
3.	Client connects to server port 8000, provides its unique identifier and gets a unique code from the server.
4.	Client connects to server port 8001, provides a text message, its identifier and code that it received on step 2.
5.	If client code does not match client identifier, server returns an error to the client.
6.	If client code is correct, server writes the provided text message to a log file.
Server should be able to simultaneously work with at least 50 clients.
It is acceptable (although not required) to use a high-level protocol (e. g. HTTP) for communication between client and server.


### requirments
First step is importing the required modules. Here, ```socket, uuid, logging``` is used to have access to operations for socket programming.

Class client_server consists of two methods called, ```server, and client```. 

### server

This method is waiting for the client to connect.

### client

This method will answer to the server and based on the port will provide information.


# How to run

Here, two main files are provided. ```main_server.py ,and  main_client.py```
When the ```main_server.py``` is running, the ```main_client.py``` must starts from the command line to conncet to the server. 