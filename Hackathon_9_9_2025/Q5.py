class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1  
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

root = Node(12)
root.left = Node(23)
root.right = Node(35)
root.left.left = Node(41)
root.left.right = Node(57)

print("Height of tree:", height(root))

