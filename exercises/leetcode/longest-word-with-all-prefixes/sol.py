class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = self.getTrie(words)
        
        dfs = [[trie, []]]
        longest = ""
        while dfs:
            cur, path = dfs.pop()

            if "#" not in cur:
                continue     

            if len(path) >= len(longest):
                possibleLongest = "".join(path)

                if len(path) == len(longest) and possibleLongest > longest:
                    pass
                else:
                    longest = possibleLongest
                
            
            # print(path)
            # if path and path[0] == 'z':
            #     print("asdasd")
            for nextC in cur:
                if nextC == "#":
                    continue
                dfs.append([cur[nextC], path + [nextC]])
    
        print(longest)
        return longest

    def getTrie(self, words: List[str]):
        trie = {"#": True}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = True
        return trie

        