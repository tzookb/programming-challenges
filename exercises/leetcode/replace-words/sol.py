from typing import List

class Solution:
    def buildTrie(self, dictionary: List[str]) -> object:
        trie = {}
        for word in dictionary:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["##"] = True
        
        return trie

    def getShortestPrefixOrWord(self, trie: object, word: str) -> str:
        cur_trie = trie
        prefixed = []

        for c in word:
            if "##" in cur_trie:
                return "".join(prefixed)
            if c not in cur_trie:
                return word
            cur_trie = cur_trie[c]
            prefixed.append(c)

        if "##" in cur_trie:
            return "".join(prefixed)
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = self.buildTrie(dictionary)
        chunked = sentence.split(" ")
        result = []

        for i in range(len(chunked)):
            word = chunked[i]
            prefix_or_word = self.getShortestPrefixOrWord(trie, word)
            result.append(prefix_or_word)

        return " ".join(result)


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

s = Solution()
res = s.replaceWords(dictionary, sentence)
print(res)
