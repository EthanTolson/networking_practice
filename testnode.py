import socket

class testnode():
    def __init__(self, ip, port, window):
        self.window = window
        self.port = port
        self.host = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))

    def connect_to_node(self, ip, port):
        self.connectedaddress = (ip, port)

    def send_message(self, message):
        self.sock.sendto(message.encode("utf-8"), self.connectedaddress)

    def get_message(self):
        message, address = self.sock.recvfrom(1024)
        return address, message.decode('utf-8')

    def listen(self):
        while True:
            address, message = self.get_message()
            self.window.label2.config(text = f"{address}: {message}")