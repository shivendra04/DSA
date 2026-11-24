class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    stack = []
    if root is None:
        return 
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            node = stack.pop()
            print(node.val, end = ",")
            root = node.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)