from pickletools import TAKEN_FROM_ARGUMENT1


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


# binary tree Depth First Traversal
def TreeDFS(root):
    stk = [root]
    while stk:
        curr = stk.pop()
        print(curr.val)
        if curr.right:
            stk.append(curr.right)
        if curr.left:
            stk.append(curr.left)
        


# binary tree Depth First Search

def TreeDFSearch(root, target):
    stk = [root]
    while stk:
        node = stk.pop()
        if node.val == target:
            return True
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
            
# binary tree Breadth First Search

def TreeBFSearch(root, target):
    from collections import deque
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node.val == target:
            return True 
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# sum of all nodes within a tree 
def TreeSum(root):
    if not root:
        return 0
    stk = [root]
    summation = 0
    while stk:
        node = stk.pop()
        summation += node.val
        if node.left:
            stk.append(node.left)
        if node.right:
            stk.append(node.right)
    return summation

#minimum node value within a tree
def TreeMin(root):
    if not root:
        return None
    minimum = float('inf')
    stk = [root]
    while stk:
        curr = stk.pop()
        minimum = min(minimum, curr.val)
        if curr.left:
            stk.append(curr.left)
        if curr.right:
            stk.append(curr.right)
    return minimum 