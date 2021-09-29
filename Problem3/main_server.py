from client_server import server_client

if __name__=='__main__':

    ports = [8000, 8001]
    host = "localhost"

    serv_cli = server_client(host, 8001)
    serv_cli.server()