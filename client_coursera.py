from time import time
import socket


class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((self.ip, self.port), self.timeout)

    @staticmethod
    def _validation_server_type_usage(server_type_usage):
        server, type = server_type_usage.split('.')
        servers = ['palm', 'eardrum']
        type_action = ['cpu', 'usage', 'disk_usage', 'network_usage']
        if server not in servers or type not in type_action:
            return False

        return True

    def put(self, server_type_usage, usage, timestamp=None):
        if timestamp is None:
            timestamp = int(time())

        if self._validation_server_type_usage(server_type_usage):
            data = server_type_usage.encode() + b':' + str(usage).encode() + b':' + str(timestamp).encode()
            self.sock.send(data)

        else:
            raise ClientError

    def get(self):
        pass


class ClientError(Exception):
    pass
