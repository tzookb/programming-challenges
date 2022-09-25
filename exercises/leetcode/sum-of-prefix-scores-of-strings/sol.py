from typing import Counter, List
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = self.buildTrie(words)
        result = []
        for word in words:
            cur_trie = trie
            total = 0
            for c in word:
                total += cur_trie[c]["#"]
                cur_trie = cur_trie[c]
            result.append(total)
        return result

    def buildTrie(self, words: List[str]):
        trie = {}
        for word in words:
            cur_trie = trie
            for c in word:
                if c not in cur_trie:
                    cur_trie[c] = {"#": 0}
                cur_trie[c]["#"] += 1
                cur_trie = cur_trie[c]
            cur_trie["##"] = True
        return trie
