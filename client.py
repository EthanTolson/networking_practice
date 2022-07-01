import socket

class Client():
    def __init__(self, ip, port, id, window):
        # window object so that you can edit text on screen
        self.window = window
        # id of the node 
        self.id = id

        self.port = port
        self.host = ip

        #create a socket and bind it to the ip and port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))

    def connect_to_node(self, ip, port):
        self.connectednodeid = None
        self.connectedaddress = (ip, port)
        # waits until the connection is made
        while self.connectednodeid == None:
            # send the id of this node to the connected node
            self.sock.sendto(self.id.encode('utf-8'), self.connectedaddress)
            # recieves the id of the connected node
            id = self.sock.recv(1024).decode('utf-8')
            self.connectednodeid = id

    def send_message(self, message):
        # Sends message and appends messages in the window
        self.sock.sendto(message.encode("utf-8"), self.connectedaddress)
        if len(self.window.messages) >= 7:
            self.window.messages.popleft()
            self.window.messages.append(f"You: {message}")
        else:
            self.window.messages.append(f"You: {message}")
        # redraws the screen so new messages appear
        self.window.redrawmessages()

    def get_message(self):
        # recieves messages from the connected node and decodes them
        message, address = self.sock.recvfrom(1024)
        return address, message.decode('utf-8')

    def listen(self):
        # function to listen for messages on a seperate thread
        while True:
            address, message = self.get_message()
            if len(self.window.messages) >= 7:
                self.window.messages.popleft()
                self.window.messages.append(f"{self.connectednodeid}: {message}")
            else:
                self.window.messages.append(f"{self.connectednodeid}: {message}")
            self.window.redrawmessages()