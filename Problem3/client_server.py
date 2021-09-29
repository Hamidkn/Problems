import socket, logging, uuid, pickle


class server_client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_address = None
        self.log_file = 'log.txt'
        logging.basicConfig(filename=self.log_file,format='%(asctime)s %(message)s')
        self.logger = logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        self.backlog = 50 # the max no of the connections(multiple clients)
        self.data_payload = 5000
    
    def server(self):

            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_address = (self.host, self.port)
            self.logger.info("Starting to connect.")
            self.socket.bind(self.server_address)
            self.socket.listen(self.backlog)
            self.unique_id_server = uuid.uuid1()

            while True:
                self.logger.info("Waiting for recieving message from the client.")
                
                client, address = self.socket.accept()
                data = client.recv(self.data_payload)
                    # if data:
                    # self.logger.info("Data: " + data)
                client.send(data)
                self.logger.info(f"send {data}, and {self.unique_id_server} bytes back to {address}")
            
                client.close()
    
    def client(self):
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_server_address = (self.host, self.port)
            self.logger.info("Starting to connect.")
            self.client_socket.connect(self.client_server_address)
        
            self.unique_id = uuid.uuid1()

            if self.port == 8000:
                try:

                    self.logger.info(f"sending unique id : {self.unique_id}")
                    self.client_socket.sendall(self.unique_id)
                    amount_received = 0
                    amount_expected = len(self.unique_id)
                    while amount_received < amount_expected:
                        data = self.client_socket.recv(self.data_payload)
                        amount_received += len(data)
                        self.logger.info(f"Received: {data}")

                except Exception:
                    self.logger.warning("Socket error")
                finally:
                    self.logger.info("Closing connection to the server")
                    self.client_socket.close()

            elif self.port == 8001:
                try:
                    message = "Hello, World!"
                    self.logger.info(f"sending {message}") 
                    # self.client_socket.sendall(message)

                    # print(self.unique_id)
                    self.logger.info(f"sending unique id : {self.unique_id}")
                    # array = f'{message} , {self.unique_id.hex} , {self.unique_id_server.hex}'
                    # print(array)
                    # data_str = pickle.dumps(array)
                    self.client_socket.sendall(str.encode("\n".join([message, str(self.unique_id), str(self.unique_id_server)])))
                    self.logger.info(f"send {message}, {self.unique_id}, {self.unique_id_server} bytes back to server.")
                    amount_received = 0
                    amount_expected = len(self.unique_id)
                    while amount_received < amount_expected:
                        data = self.client_socket.recv(self.data_payload)
                        amount_received += len(data)
                        self.logger.info(f"Received: {data}")

                except Exception:
                    self.logger.warning("Socket error")
                finally:
                    self.logger.info("Closing connection to the server")
                    self.client_socket.close()