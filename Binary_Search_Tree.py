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
        print("Value not found in the tree")
        return

    if root.data == value:
        print("Value found in the tree")
        return

    if root.data > value:
        search(root.left, value)
    else:
        search(root.right, value)


def get_successor(root):
    root = root.right

    while root is not None and root.left is not None:
        root = root.left

    return root


def delete(root, value):
    if root is None:
        return None

    if root.data > value:
        root.left = delete(root.left, value)

    elif root.data < value:
        root.right = delete(root.right, value)

    else:
        # Case 1: No left child
        if root.left is None:
            return root.right

        # Case 2: No right child
        elif root.right is None:
            return root.left

        # Case 3: Two children
        else:
            successor = get_successor(root)
            root.data = successor.data
            root.right = delete(root.right, successor.data)

    return root


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

print("Before deletion:")
inorder(root)

root = delete(root, 40)

print("\nAfter deleting 40:")
inorder(root)

print()