class MapSum:

    def __init__(self):
        self.data = {}
        self.vals = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.vals.get(key, 0)
        self.vals[key] = val
        cur_step = self.data
        for c in key:
            if c not in cur_step:
                cur_step[c] = {
                    "##": 0
                }
            cur_step[c]["##"] += diff
            cur_step = cur_step[c]
    
    def sum(self, prefix: str) -> int:
        cur_step = self.data
        for c in prefix:
            if c not in cur_step:
                return 0
            cur_step = cur_step[c]
        return cur_step["##"]
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)