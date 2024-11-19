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


def print_tree_2d(root, level=0, space=4):
    if root is None:
        return
    # Zwiększ poziom odstępu
    level += space
    # Wypisz prawe poddrzewo najpierw
    print_tree_2d(root.right, level)
    # Wypisz bieżący węzeł
    print(" " * (level - space) + str(root.val))
    # Wypisz lewe poddrzewo
    print_tree_2d(root.left, level)


r = Node(50)
add(25,r)
add(26,r)
add(22,r)
add(71,r)
add(51,r)
# print(r)
print_tree_2d(r)


