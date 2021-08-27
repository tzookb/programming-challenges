class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        chars = list(word)
        cur_step = self.data
        for char in chars:
            if char not in cur_step:
                cur_step[char] = {}
            cur_step = cur_step[char]
        cur_step["##"] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_step = self.startsWith(word)
        if cur_step is False:
            return False
        return "##" in cur_step
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        chars = list(prefix)
        cur_step = self.data
        for char in chars:
            if char not in cur_step:
                return False
            cur_step = cur_step[char]
        return cur_step
        
