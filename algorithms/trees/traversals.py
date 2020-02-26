class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return self.val

root = TreeNode(1)
root_left = TreeNode(2)
root_right = TreeNode(3)
root_left_left = TreeNode(4)
root_left_right = TreeNode(5)
root_right_left = TreeNode(6)
root_right_right = TreeNode(7)
root.left = root_left
root.right = root_right
root_left.left = root_left_left
root_left.right = root_left_right
root_right.left = root_right_left
root_right.right = root_right_right

def tree_inorder(tree):
    res = []
    if tree:
        res = tree_inorder(tree.left)
        res.append(tree.val)
        res = res + (tree_inorder(tree.right))
    return res

def tree_preorder(tree):
    res = []
    if tree:
        res.append(tree.val)
        res = res + tree_preorder(tree.left)
        res = res + tree_preorder(tree.right)
    return res

def tree_postorder(tree):
    res = []
    if tree:
        res = res + tree_postorder(tree.left)
        res = res + tree_postorder(tree.right)
        res.append(tree.val)
    return res
def tree_to_arr(tree):
    final = []
    stack = [tree]
    while stack:
        cur = stack.pop(0)
        if not cur:
            final.append(None)
            continue
        final.append(cur.val)
        stack.append(cur.left)
        stack.append(cur.right)

    last_none = -1
    for idx, item in enumerate(final):
        if item is None and last_none == -1:
            last_none = idx
        if item:
            last_none = -1
    
    if last_none != -1:
        final = final[0:last_none]

    return final


arr = tree_postorder(root)
print(arr)