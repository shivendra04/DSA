from collections import deque as dq
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root):
    if root is None:
        return
    que = dq([root])
    while que:
        level = []
        for i in range(len(que)):
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            level.append(node.val)
        print(level)
            


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


level_order(root)