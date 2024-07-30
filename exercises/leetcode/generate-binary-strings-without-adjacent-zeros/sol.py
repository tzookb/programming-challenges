class Solution:
    def validStrings(self, n: int) -> List[str]:
        items = ["0", "1"]
        if n == 1:
            return items

        # 0, 1
        # 01,10,11
        for _ in range(n - 1):
            next_items = []
            for item in items:
                if item[-1] == "1":
                    next_items.append(item + "0")
                next_items.append(item + "1")
            items = next_items

        return items