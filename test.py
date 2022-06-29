from mynode import MyNode
from time import sleep

newnode = MyNode("127.0.0.1", 10001)
sleep(1)
node2 = MyNode("127.0.0.1", 10002)
newnode.start()
sleep(1)
node2.start()
sleep(1)
newnode.connect_with_node("127.0.0.1", 10002)
sleep(2)

newnode.send_to_nodes({"message": "Hello There", "sentfrom":newnode.id})
x = 1

while x != 'q':
    x = input("Enter Message: ")
    newnode.send_to_nodes({"message": str(x), "sentfrom" : newnode.id})

newnode.stop()
node2.stop()