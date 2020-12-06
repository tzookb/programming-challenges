def visible_nodes(root):
    nodes = [(root, 1)]
    max_level = 0
    while nodes:
        node, level = nodes.pop()
        max_level = max(max_level, level)
        if node.left:
            nodes.append((node.left, level + 1))
        if node.right:
            nodes.append((node.right, level + 1))

    return max_level

def visible_nodes_recu(root):
    def recu(node):
        if not node:
            return 0
        left_level = 1
        right_level = 1
        if node.left:
            left_level = recu(node.left) + 1
        if node.right:
            right_level = recu(node.right) + 1

        return max(left_level, right_level)

    return recu(root)
