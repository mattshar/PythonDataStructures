class Node:
    def __init__(self, data):
        self.data = data 
        self.next = next

        # singly
class LinkedList:
    def __init__(self):
        self.head = None

    def appendNode(self, data):
        addedNode = Node(data)

        if not self.head:
            self.head = addedNode
            return 

        current = self.head
        while current.next:
            current = current.next 

        current.next = addedNode

    def delete(self, data):
        if not self.head:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next



    # doubly linked list implementation 

class NodeDoubly:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None # backward facing pointer

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append2(self, data):
        next_node = NodeDoubly(data)

        if not self.head:
            self.head = next_node
            return 
        current = self.head # iterator node 
        while current:
            current = current.next 
        # by the time this loop breaks, we have a reference to the current ending node 

        current.next = next_node
        next_node.prev = current 

