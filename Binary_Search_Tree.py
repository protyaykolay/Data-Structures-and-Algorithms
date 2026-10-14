class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if root is None:
        return Node(value)

    if root.data == value:
        return root

    if root.data > value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def search(root, value):
    if root is None:
        print("Value not found in the tree", end="\n")
        return

    if root.data == value:
        print("Value found in the tree", end="\n")
        return

    if root.data > value:
        search(root.left, value)
    else:
        search(root.right, value)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)

inorder(root)
print("\n")

search(root, 18)
search(root, 100)