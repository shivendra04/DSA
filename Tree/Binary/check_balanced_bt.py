class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_depth(root):
    if root is None:
        return 0
    return 1 + max(find_depth(root.left), find_depth(root.right))

def check_balanced_bt(root):
    if root is None:
        return True
    lh = find_depth(root.left)
    rh = find_depth(root.right)
    if abs(lh-rh)>1:
        return False
    left_check = check_balanced_bt(root.left)
    right_check = check_balanced_bt(root.right)
    if not left_check or not right_check:
        return False
    return True


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(check_balanced_bt(root))