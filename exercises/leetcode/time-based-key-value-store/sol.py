class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.spots = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.spots:
            self.spots[key] = []
        
        self.spots[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.spots:
            return ""

        vals = self.spots[key]
        i = len(vals) - 1
        while i >= 0:
            cur_stamp, cur_val = vals[i]
            if timestamp >= cur_stamp:
                return cur_val
            i -= 1

        return ""
        
        