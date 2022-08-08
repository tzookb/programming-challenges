from typing import List
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        arr = []
        if not root:
            return ""
        nodes = [(root, 1)]
        while nodes:
            node, idx = nodes.pop(0)
            if not node:
                arr.append(None)
                continue
            arr.append((node, idx))
            nodes.append((node.left, idx * 2))
            nodes.append((node.right, idx * 2 + 1))

        
        
        res = []
        for item in arr:
            if item is None:
                continue
            
            res.append(f"{item[1]}*{item[0].val}")

        raw = "_".join(res)
        return raw
        

    def deserialize(self, data):
        if data == "":
            return None
        itemsraw = data.split("_")
        data = list(map(lambda x: x.split("*"), itemsraw))
        mapped = {}
        for idx, item in data:
            mapped[idx] = item
        
        def build(idx):
            if not mapped.keys():
                return None
            if str(idx) not in mapped:
                return None

            cur = TreeNode(int(mapped[str(idx)]))
            del mapped[str(idx)]
            left = build(idx * 2) 
            right = build(idx * 2 + 1) 


            cur.left = left
            cur.right = right
            
            return cur

        return build(1)
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
