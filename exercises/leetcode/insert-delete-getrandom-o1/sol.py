import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data:
            self.data[val] = True
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            del self.data[val]
            return True
        return False
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        vals = list(self.data.keys())
        size = len(vals)
        rand_idx = random.randint(0, size-1)
        return vals[rand_idx]
