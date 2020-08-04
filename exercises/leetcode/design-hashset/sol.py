class MyHashSet:

    def __init__(self):
        self.data = {}
        pass

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.data[key]

    def contains(self, key: int) -> bool:
        return key in self.data