import tkinter as tk

class display():
    def __init__(self):
        # create tkinter object set the title and create a database creation object to work with the database
        self.window = tk.Tk()
        self.window.title("Messaging Application")
        self.window.state('zoomed')
        self.window.geometry("500x500")

    def draw_interface(self):
        self.loginbutton = tk.Button(text = "Login", background = "#259c45", activebackground = "#2621ad", font = 3, width = 10, height = 1, command = self.login)
        self.username = tk.Entry()
        self.passwordentry = tk.Entry()
        self.label1 = tk.Label(text = "Username: ")
        self.label2 = tk.Label(text = "Password: ")
        self.label3 = tk.Label(text = "")

        self.label1.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.username.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.label2.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.passwordentry.grid(row = 2, column = 2, padx = 10, pady = 10)
        self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
        self.loginbutton.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10)

    def login(self):
        if self.username.get() == "admin" and self.passwordentry.get() == "12345":
            self.adminview()
        if self.username.get() == "" or self.passwordentry.get() == "":
            self.label3.destroy()
            self.label3 = tk.Label(text = "Please enter a Username and/or Password.")
            self.label3.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)

    def adminview(self):
        pass

    def messaging_view(self):
        pass