import tkinter as tk
import threading
import client
from collections import deque

class display():
    def __init__(self):
        # create tkinter object set the title
        self.window = tk.Tk()
        self.window.title("Messaging Application")
        self.window.state('zoomed')
        self.window.geometry("500x500")
        # Define what happens when window closes
        self.window.protocol("WM_DELETE_WINDOW", self.exit)
        # Use a queue to hold the messages
        self.messages = deque()
        self.node = None

    def exit(self):
        # What happens when window is closed
        self.window.destroy()

    def draw_interface(self):
        # Buttons, entries, and labels that allow the user to create a connection
        self.loginbutton = tk.Button(text = "Login", background = "#259c45", activebackground = "#2621ad", font = 3, width = 10, height = 1, command = self.login)
        self.username = tk.Entry()
        self.label1 = tk.Label(text = "Username: ")

        self.ip = tk.Entry()
        self.port = tk.Entry()
        self.label4 = tk.Label(text = "IP Address: ")
        self.label5 = tk.Label(text = "Port: ")

        self.label3 = tk.Label(text = "")

        # Pack the buttons, labels and entries to the screen
        self.label1.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.username.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        self.label4.grid(row = 1, column = 3, padx = 10, pady = 10)
        self.ip.grid(row = 1, column = 4, padx = 10, pady = 10)
        self.label5.grid(row = 2, column = 3, padx = 10, pady = 10)
        self.port.grid(row = 2, column = 4, padx = 10, pady = 10)
        self.loginbutton.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10)

    def login(self):
        # Checks to make sure user can create a connection and that they filled out each entry
        if self.username.get() == "":
            self.label3.destroy()
            self.label3 = tk.Label(text = "Please enter an Username and/or Password.")
            self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        elif self.ip.get() == "" or self.port.get() == "":
            self.label3.destroy()
            self.label3 = tk.Label(text = "Please enter an IP and/or Port Number.")
            self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        else:
            try:
                # Try to create a connection from the test node class
                self.node = client.Client(self.ip.get(), int(self.port.get()), id = self.username.get(), window = self)
                # Changes the view after the connection has been created
                self.connectionscreen()
            except:
                self.label3.destroy()
                self.label3 = tk.Label(text = "Falied to create node.")
                self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)

    def connectionscreen(self):
        # Clear the screen
        self.loginbutton.destroy()
        self.label1.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.username.destroy()
        self.port.destroy()
        self.ip.destroy()

        # Setup entries and buttons so that user can connect with another node
        self.ip = tk.Entry()
        self.port = tk.Entry()
        self.label1 = tk.Label(text = "IP Address: ")
        self.label2 = tk.Label(text = "Port: ")
        self.label3 = tk.Label(text = "Enter information of Node you want to connect to.")
        self.connectbutton = tk.Button(text = "Try to Connect", background = "#259c45", activebackground = "#2621ad", font = 3, width = 20, height = 1, command = self.testConnection)

        # Pack everything to the screen
        self.label1.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.ip.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.label2.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.port.grid(row = 2, column = 2, padx = 10, pady = 10)
        self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        self.connectbutton.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10)

    def testConnection(self):
        # Makes sure that you can connect and siwtches the view after you have made a connection
        if self.ip.get() == "" or self.port.get() == "":
            self.label3.destroy()
            self.label3 = tk.Label(text = "Please enter an IP and/or Port Number.")
            self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        elif str(self.node.port) == self.port.get() and self.node.host == self.ip.get():
            self.label3.destroy()
            self.label3 = tk.Label(text = "Cannot connect with yourself.")
            self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        else:
            try:
                self.node.connect_to_node(self.ip.get(), int(self.port.get()))
                # thread listens for messages recieved
                self.thread1 = threading.Thread(target = self.node.listen, daemon = True)
                self.thread1.start()
            except:
                self.label3.destroy()
                self.label3 = tk.Label(text = "Falied to connect to node.")
                self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
            self.messaging_view()

    def messaging_view(self):
        # Clear the screen
        self.connectbutton.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.port.destroy()
        self.ip.destroy()

        #Create labels entries and buttons for messaging

        self.label1 = tk.Label(text = f"You are currently connected with {self.node.connectedaddress[0]}, {self.node.connectedaddress[1]}")

        self.labels = [tk.Label(text = ""), tk.Label(text = ""), tk.Label(text = ""), tk.Label(text = ""), tk.Label(text = ""), tk.Label(text = ""), tk.Label(text = "")]

        self.messageentry = tk.Entry(width = 70)
        self.sendbutton = tk.Button(text = "Send Message", background = "#259c45", activebackground = "#2621ad", font = 3, width = 30, height = 1, command = self.sendmessage)
        i = 2
        for label in self.labels:
            label.grid(row = i, column = 1, columnspan = 5, padx = 10, pady = 10)
            i += 1

        self.label1.grid(row = 1, column = 1, columnspan = 5, padx = 10, pady = 10)

        self.messageentry.grid(row = 9, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.sendbutton.grid(row = 9, column = 6, columnspan = 3, padx = 10, pady = 10)

    def sendmessage(self):
        # Sends the message through the node class and clears the entry box
        self.node.send_message(self.messageentry.get())
        self.messageentry.delete(0, tk.END)

    def redrawmessages(self):
        # Edits the labels as messages are sent and recieved
        i = 0
        for message in self.messages:
            self.labels[i].config(text = message)
            i += 1    