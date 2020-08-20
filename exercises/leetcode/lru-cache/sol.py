from typing import List

class Node:
    def __init__(self, key, dataval=None):
        self.key = key
        self.val = dataval
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head = Node(None)
        self.last = Node(None)
        self.head.next = self.last
        self.last.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.extract(node)
        self.attachToStart(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.extract(node)
            self.attachToStart(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self.attachToStart(node)
        self.size += 1

        if self.size > self.cap:
            self.removeLast()
            self.size -= 1

    def removeLast(self) -> None:
        node = self.last.prev
        self.extract(node)
        del self.cache[node.key]

    def attachToStart(self, node) -> None:
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextNode
        nextNode.prev = node
        
        
    def extract(self, node) -> None:
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
