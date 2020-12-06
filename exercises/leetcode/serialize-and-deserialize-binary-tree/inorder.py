class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

def treeToArrPreOrder(root):
    arr = []
    nodes = [root]
    while nodes:
        cur = nodes.pop(0)
        if not cur:
            arr.append(None)
            continue

        arr.append(cur.val)
        nodes.insert(0, cur.right)
        nodes.insert(0, cur.left)
    return arr


def arrToTreePreOrder(arr):
    if not arr:
        return (None, [])
    val = arr.pop(0)
    if not val:
        return (None, arr)
    curNode = TreeNode(val)

    leftBranch, leftArr = arrToTreePreOrder(arr)
    curNode.left = leftBranch
    rightBranch, leftArr = arrToTreePreOrder(leftArr)
    curNode.right = rightBranch
    return (curNode, leftArr)

def printTree(root):
    nodes = [(root, 1)]
    curLevel = 1
    items = []
    while nodes:
        cur, level = nodes.pop(0)
        if level != curLevel:
            print(items)
            curLevel = level
            items = []
        if not cur:
            items.append("_")
            continue
        items.append(cur.val)
        nodes.append((cur.left, level + 1))
        nodes.append((cur.right, level + 1))
    
    print(items)

arr = [100,50,25,None,None,75,None,None,200,None,350,None,None]
tree, arr = arrToTreePreOrder(arr)
revArr = treeToArrPreOrder(tree)
print(revArr)