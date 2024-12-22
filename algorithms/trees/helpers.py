from typing import List
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
    
    while final and final[-1] == None:
        final.pop()

    return final

def arr_to_tree(arr: List[int]):
    if not arr:
        return None
    head = TreeNode(arr.pop(0))
    
    stack = [head]
    while arr:
        cur_val = arr.pop(0)
        cur = TreeNode(cur_val)
        cur_tree = stack.pop
    return stack