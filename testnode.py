import socket

class testnode():
    def __init__(self, ip, port, id, window):
        self.window = window
        self.id = id
        self.port = port
        self.host = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))

    def connect_to_node(self, ip, port):
        self.connectednodeid = None
        self.connectedaddress = (ip, port)
        while self.connectednodeid == None:
            self.sock.sendto(self.id.encode('utf-8'), self.connectedaddress)
            id = self.sock.recv(1024).decode('utf-8')
            self.connectednodeid = id

    def send_message(self, message):
        self.sock.sendto(message.encode("utf-8"), self.connectedaddress)
        if len(self.window.messages) >= 7:
            self.window.messages.popleft()
            self.window.messages.append(f"You: {message}")
        else:
            self.window.messages.append(f"You: {message}")
        self.window.redrawmessages()

    def get_message(self):
        message, address = self.sock.recvfrom(1024)
        return address, message.decode('utf-8')

    def listen(self):
        while True:
            address, message = self.get_message()
            if len(self.window.messages) >= 7:
                self.window.messages.popleft()
                self.window.messages.append(f"{self.connectednodeid}: {message}")
            else:
                self.window.messages.append(f"{self.connectednodeid}: {message}")
            self.window.redrawmessages()