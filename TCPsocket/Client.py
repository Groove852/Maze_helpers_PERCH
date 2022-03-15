import socket
import subprocess


class Client(object):
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, ip):
        self._socket.connect((ip, 8888))
        return

    def start(self):
        while 1:
            value = self._socket.recv(1024).decode()
            if value == "1":
                self.command()
            elif value == "2":
                self.sendDiagnostic()
            elif value == "3":
                self.sendTopics()
            elif value == "exit":
                break
            else:
                continue
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



