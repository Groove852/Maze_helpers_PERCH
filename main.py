from TCPsocket.Server import Server
from TCPsocket.Client import Client

server = Server('127.0.0.1')
client = Client('127.0.0.1')


def main():
    server.start()
    client.start()


if __name__ == '__main__':
    main()
