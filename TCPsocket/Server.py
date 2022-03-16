import socket


class Server(object):
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _value = '0'
    _topic = '0'
    _cmd = '0'

    def __init__(self, ip, listeners=5):
        self._socket.bind((ip, 8888))
        self._socket.listen(listeners)
        self.__client, self.__adr = self._socket.accept()
        return

    def start(self):
        while 1:
            self._value = self.__client.recv(1024).decode()
            if self._value == '1':
                self._cmd = str(input("Enter command:"))
                self.command(self._cmd)

            elif self._value == '2':
                self.getDiagnostic()

            elif self._value == '3':
                if self._topic == '0':
                    self._topic = str(input("Enter topic"))
                self.getTopics(self._topic)

        self.__client.close()

    """def getDiagnostic(self):
        return

    def getTopics(self, topic):
        try:
            self.__client.send(topic.encode())
            result_output = self.__client.recv(1024).decode()
            print(result_output)
        finally:
            pass"""

    def command(self, command):
        try:
            self.__client.send(command.encode())
            result_output = self.__client.recv(1024).decode()
            print(result_output)
        finally:
            pass

