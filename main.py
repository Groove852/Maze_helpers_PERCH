from TCPsocket.Server import Server
from TCPsocket.ClientCommand import Client
import socket
server = Server('127.0.0.1')
client = Client('127.0.0.1')


def main():
    server.start()
    client.start()


if __name__ == '__main__':
    main()
