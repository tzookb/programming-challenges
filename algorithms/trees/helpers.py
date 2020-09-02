class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return self.val

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
    return stack