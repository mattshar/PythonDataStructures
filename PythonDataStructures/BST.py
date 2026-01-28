class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)


def balance(self):
    # 1. Turn the tree into a simple sorted array / list of values
    vals = []

    def pull_vals(node):
        if node:
            pull_vals(node.left)
            vals.append(node.value)
            pull_vals(node.right)

    pull_vals(self.root)

    if not vals:
        return

    # 2  Separate Function to rebuild a balanced tree from that list
    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        root = Node(vals[mid])  # Middle becomes the new parent
        root.left = build(lo, mid - 1)      # Left half becomes left child
        root.right = build(mid + 1, hi)     # Right half becomes right child
        return root

    self.root = build(0, len(vals) - 1)






