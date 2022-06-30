import tkinter as tk
import threading
import testnode

class display():
    def __init__(self):
        # create tkinter object set the title and create a database creation object to work with the database
        self.window = tk.Tk()
        self.window.title("Messaging Application")
        self.window.state('zoomed')
        self.window.geometry("500x500")
        self.window.protocol("WM_DELETE_WINDOW", self.exit)
        self.node = None

    def exit(self):
        self.window.destroy()

    def draw_interface(self):
        self.loginbutton = tk.Button(text = "Login", background = "#259c45", activebackground = "#2621ad", font = 3, width = 10, height = 1, command = self.login)
        self.username = tk.Entry()
        self.passwordentry = tk.Entry()
        self.label1 = tk.Label(text = "Username: ")
        self.label2 = tk.Label(text = "Password: ")

        self.ip = tk.Entry()
        self.port = tk.Entry()
        self.label4 = tk.Label(text = "IP Address: ")
        self.label5 = tk.Label(text = "Port: ")

        self.label3 = tk.Label(text = "")

        self.label1.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.username.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.label2.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.passwordentry.grid(row = 2, column = 2, padx = 10, pady = 10)
        self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        self.label4.grid(row = 1, column = 3, padx = 10, pady = 10)
        self.ip.grid(row = 1, column = 4, padx = 10, pady = 10)
        self.label5.grid(row = 2, column = 3, padx = 10, pady = 10)
        self.port.grid(row = 2, column = 4, padx = 10, pady = 10)
        self.loginbutton.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10)

    def login(self):
        if self.username.get() == "admin" and self.passwordentry.get() == "12345":
            self.adminview()
            return
        if self.username.get() == "" or self.passwordentry.get() == "":
            self.label3.destroy()
            self.label3 = tk.Label(text = "Please enter an Username and/or Password.")
            self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        elif self.ip.get() == "" or self.port.get() == "":
            self.label3.destroy()
            self.label3 = tk.Label(text = "Please enter an IP and/or Port Number.")
            self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        else:
            try:
                #self.node = mynode.MyNode(self.ip.get(), int(self.port.get()), id = self.username.get(), window = self)
                self.node = testnode.testnode(self.ip.get(), int(self.port.get()), window = self)
                self.connectionscreen()
            except:
                self.label3.destroy()
                self.label3 = tk.Label(text = "Falied to create node.")
                self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)

    def adminview(self):
        pass

    def connectionscreen(self):
        self.loginbutton.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.passwordentry.destroy()
        self.username.destroy()
        self.port.destroy()
        self.ip.destroy()

        self.ip = tk.Entry()
        self.port = tk.Entry()
        self.label1 = tk.Label(text = "IP Address: ")
        self.label2 = tk.Label(text = "Port: ")
        self.label3 = tk.Label(text = "Enter information of Node you want to connect to.")
        self.connectbutton = tk.Button(text = "Try to Connect", background = "#259c45", activebackground = "#2621ad", font = 3, width = 20, height = 1, command = self.testConnection)

        self.label1.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.ip.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.label2.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.port.grid(row = 2, column = 2, padx = 10, pady = 10)
        self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        self.connectbutton.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10)

    def testConnection(self):
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
                self.thread1 = threading.Thread(target = self.node.listen, daemon = True)
                self.thread1.start()
            except:
                self.label3.destroy()
                self.label3 = tk.Label(text = "Falied to connect to node.")
                self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
            self.messaging_view()

    def messaging_view(self):
        self.connectbutton.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.port.destroy()
        self.ip.destroy()

        self.label1 = tk.Label(text = f"You are currently connected with {self.node.connectedaddress[0]}, {self.node.connectedaddress[1]}")
        self.label2 = tk.Label(text = "")
        self.label3 = tk.Label(text = "")
        self.label4 = tk.Label(text = "")
        self.label5 = tk.Label(text = "")
        self.label6 = tk.Label(text = "")
        self.label7 = tk.Label(text = "")
        self.label8 = tk.Label(text = "")

        self.messageentry = tk.Entry(width = 70)
        self.sendbutton = tk.Button(text = "Send Message", background = "#259c45", activebackground = "#2621ad", font = 3, width = 30, height = 1, command = self.sendmessage)
        
        self.label1.grid(row = 1, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.label2.grid(row = 2, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.label3.grid(row = 3, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.label4.grid(row = 4, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.label5.grid(row = 5, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.label6.grid(row = 6, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.label7.grid(row = 7, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.label8.grid(row = 8, column = 1, columnspan = 5, padx = 10, pady = 10)

        self.messageentry.grid(row = 9, column = 1, columnspan = 5, padx = 10, pady = 10)
        self.sendbutton.grid(row = 9, column = 6, columnspan = 3, padx = 10, pady = 10)

    def sendmessage(self):
        self.label8.config(text = f"You: {self.messageentry.get()}")
        self.node.send_message(self.messageentry.get())
        self.messageentry.delete(0, tk.END)

    