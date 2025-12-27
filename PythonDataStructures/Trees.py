class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = None
        self.right = None 


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F


