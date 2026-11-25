class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(root):
    stack1 = []
    cur = root
    while cur or stack1:
        if cur:
            stack1.append(cur)
            cur = cur.left
        else:
            temp = stack1[-1].right
            if temp is None:
                temp = stack1.pop()
                print(temp.val,end = ",")
                while stack1 and temp == stack1[-1].right:
                    temp = stack1.pop()
                    print(temp.val, end = ",")
            else:
                cur = temp
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

postorder(root)