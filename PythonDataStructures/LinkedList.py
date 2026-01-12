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