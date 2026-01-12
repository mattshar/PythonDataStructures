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

