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


r = Node(1)
add(3,r)
add(2,r)
add(5,r)
add(3,r)
add(None,r)
add(9,r)
# print(r)
print_tree_2d(r)







class Solution(object):
    def hasPathSum(self, root, targetSum):

        def check(root,current_sum):
            if root is None:
                return False
            current_sum += root.val
            if current_sum == targetSum and root.left == None and root.right == None:
                return True
            return check(root.left,current_sum) or check(root.right,current_sum)
        return check(root,0)


# def largestValues(root):
