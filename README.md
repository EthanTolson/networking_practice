# Overview

For the past two weeks I have been putting together a simple messaging application. This application uses a peer to peer network to send and receive the messages.

## Description

My program uses tkinter to create a window where you can create a connection and connect with another peer and exchange messages. You need to know the IP and port number of the person you wish to connect to. After you connect you can send messages using the entry box and send message button.

## Why I Created It

I wanted to learn more about networking and so decided to learn a little bit about the socket library in python. I used the socket library to create a peer to peer connection then created a UI so that you could send messages across the network.

[Software Demo Video](https://youtu.be/sUA_airxfWM)

# Network Communication

I created a peer to peer connection. I am using a UDP connection and you can specify what port number to use in the program. Messages are being sent as UTF-8 encoded bytes.

# Development Environment

IDE: VS Code

Language: Python

Libraries: 
* socket
* tkinter
* threading


# Useful Websites

* [Socket Documentation](https://docs.python.org/3.6/library/socket.html)
* [UDP Peer-To-Peer Messaging With Python - Video](https://www.youtube.com/watch?v=IbzGL_tjmv4)

# Future Work

* Add a cloud database to store message history and login information
* Make the UI look better
* add support for sending things other than text