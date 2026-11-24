class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    stack = []
    if root is None:
        return 
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        print(node.val, end = ',')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder(root)