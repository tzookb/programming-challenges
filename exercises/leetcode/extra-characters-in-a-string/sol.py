class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo = {}

        def recu(phrase) -> int:
            if phrase == "":
                return 0 
            if phrase in memo:
                return memo[phrase]
            minleftover = float("inf")

            for w in dictionary:
                if len(w) > len(phrase):
                    continue
                if w != phrase[0:len(w)]:
                    continue

                leftphrase = phrase[len(w):]

                leftover = recu(leftphrase)
                minleftover = min(minleftover, leftover)
            
            minWithSkipFirst = recu(phrase[1:]) + 1
            memo[phrase] = min(minleftover, minWithSkipFirst)
            return memo[phrase]

        return recu(s)
        

        