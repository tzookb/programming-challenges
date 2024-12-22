class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            
            cur = cur[c]

        if "#" not in cur:
            cur["#"] = 0
        cur["#"] += 1
        

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.trie
        for c in word:
            if c not in cur:
                return 0
            cur = cur[c]
        if "#" not in cur:
            return 0
        return cur["#"]
        

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return 0
            cur = cur[c]
        
        prefixes = 0
        bfs = [cur]
        while bfs:
            item = bfs.pop(0)
            if "#" in item:
                prefixes += item["#"]
            
            for key in item:
                if key == "#":
                    continue
                bfs.append(item[key])
        return prefixes

    def erase(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                return 0

            cur = cur[c]
        cur["#"] -= 1
        if cur["#"] == 0:
            del cur["#"]
