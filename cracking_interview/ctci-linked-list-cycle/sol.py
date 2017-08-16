class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

d = Node('d')
c = Node('c', d)
b = Node('b', c)
a = Node('a', b)
d.next = c

def has_cycle(head):
    if head is None:
        return False
    if head.next is None:
        return False

    passed = {}
    passed[head.data] = True
    next = head.next
    

    while True:
    	key = next.data
    	
    	
    	if key in passed:
    		print key
    		return True

    	passed[key] = True

    	next = next.next
    	if next is None:
    		return False

print has_cycle(a)

# dic = {} 
# dic[1] = False
# if 1 in dic:
# 	print dic
