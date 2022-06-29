from p2pnetwork.node import Node
import tkinter as tk

class MyNode(Node):
    def __init__(self, host, port, id = None, callback = None, max_connections = 0, window = None):
        super(MyNode, self).__init__(host, port, id, callback, max_connections)
        self.window = window

    def inbound_node_connected(self, node):
        print(f"Inbound Node: {node.id} Connected.")
        return super().inbound_node_connected(node)

    def outbound_node_connected(self, node):
        print(f"Outbound Node: {node.id} Connected.")
        return super().outbound_node_connected(node)

    def inbound_node_disconnected(self, node):
        print(f"Inbound Node: {node.id} Disconnected.")
        return super().inbound_node_disconnected(node)

    def outbound_node_disconnected(self, node):
        print(f"Outbound Node: {node.id} Disconnected.")
        return super().outbound_node_disconnected(node)

    def node_message(self, node, data):
        sentfrom = data["sentfrom"]
        message = data["message"]
        self.window.label1.destroy()
        self.window.label1 = tk.Label(text = message)
        print(f"A: {sentfrom}, {message}")

    def node_disconnect_with_outbound_node(self, node):
        print("Node wants to disconnect.")
        return super().node_disconnect_with_outbound_node(node)

    def node_request_to_stop(self):
        print("Requested To Stop.")
        return super().node_request_to_stop()