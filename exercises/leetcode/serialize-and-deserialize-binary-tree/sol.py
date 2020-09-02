# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        arr = []
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            if not node:
                arr.append("null")    
                continue
            arr.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)
        
        j = len(arr) - 1
        while j >= 0:
            if arr[j] == "null":
                arr.pop()
            else:
                break
            j -= 1
            
        arr = [str(x) for x in arr]
        return arr
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data[0])
        nodes = [root]
        isFirst = True
        for v in data[1:]:
            parent = nodes[0]
            newNode = TreeNode(v)
            if isFirst:
                parent.left = newNode
                isFirst = False
            else:
                nodes.pop(0)
                parent.right = newNode
                isFirst = True
            nodes.append(newNode)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))