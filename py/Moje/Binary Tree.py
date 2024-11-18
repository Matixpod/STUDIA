class Node():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def add(key,root):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = add(key,root.left)
    elif key > root.val:
        root.right = add(key,root.right)
    return root

def print_tree(root):
    if root.left is not None:
        print_tree(root.left)
    if root.right is not None:
        print_tree(root.right)

    print(f"{root.val}")
    # return f"{root.val}"

r = Node(50)
add(25,r)
add(26,r)
add(22,r)
add(71,r)
add(51,r)
print_tree(r)


# print(r.val,r.left,r.right)
# print(r.left.val,r.left.left,r.left.right)
# print(r.left.left.val,r.left.left.left,r.left.left.right)

print(r)


