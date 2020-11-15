class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curTrie = self.trie
        for c in word:
            if c not in curTrie:
                curTrie[c] = {}
            curTrie = curTrie[c]
        curTrie["next"] = None

    def rec_search(self, word: str, trie) -> bool:
        if not word:
            return "next" in trie

        c = word[0]
        left = word[1:]
        if c in trie:
            return self.rec_search(left, trie[c])

        if c == ".":
            for key in trie:
                if key == "next":
                    continue
                temp = self.rec_search(left, trie[key])
                if temp:
                    return True

        return False

    def search(self, word: str) -> bool:
        curTrie = self.trie
        return self.rec_search(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
obj.addWord("a")
res = obj.search("a.")
print(res)