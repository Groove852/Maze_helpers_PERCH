import socket
import subprocess


class Client(object):
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self._socket.connect((input("Enter IP:\n"), input("Enter Port: \n")))
        return

    def start(self):
        while 1:
            self._socket.send('1'.encode())
            self.command()
        self._socket.close()

    def sendDiagnostic(self):
        return

    def sendTopics(self):
        topic = self._socket.recv(1024).decode()
        output = subprocess.getoutput(f'rostopic echo /{topic}')
        self._socket.send(output.encode())

    def command(self):
        command = self._socket.recv(1024).decode()
        output = subprocess.getoutput(command)
        self._socket.send(output.encode())


client = Client()
client.start()
