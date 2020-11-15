
class Solution:
    def __init__(self):
        super().__init__()
        self.sols = set()
        self.removals = 0
        self.checked = {}

    def isValid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
            if count < 0:
                return False
        return count == 0

    def isBracket(self, c):
        return c == ")" or c == "("

    def solve(self, s, leftOpeners, leftClosers):
        cachKey = s+"_"+str(leftOpeners)+"_"+str(leftClosers)
        if cachKey in self.checked:
            return
        
        self.checked[cachKey] = True
        if leftOpeners + leftClosers == 0:
            if self.isValid(s):
                self.sols.add(s)
            return

        for i in range(0, len(s)):
            if not self.isBracket(s[i]):
                continue
            if s[i] == "(" and leftOpeners == 0:
                continue
            if s[i] == ")" and leftClosers == 0:
                continue
            start = s[0:i]
            end = s[i+1:]
            merged = start + end

            nextLeftOpeners = leftOpeners -1 if s[i] == "(" else leftOpeners
            nextLeftClosers = leftClosers -1 if s[i] == ")" else leftClosers
            self.solve(merged, nextLeftOpeners, nextLeftClosers)
            

    def trimEnds(self, s):
        length = len(s)
        i = 0
        leftTrim = 0
        rightTrim = 0
        while i < length:
            if s[i] == ")":
                leftTrim += 1
            else:
                break
            i += 1
        i = length - 1
        while i >= 0:
            if s[i] == "(":
                rightTrim += 1
            else:
                break
            i -= 1
        
        return s[leftTrim : length - rightTrim]

    def removeInvalidParentheses(self, s):
        cleanedS = self.trimEnds(s)
        removals = self.getRemovals(cleanedS)
        self.solve(cleanedS, removals[0], removals[1])
        return list(self.sols)

    def getRemovals(self, s: str) -> int:
        removalsClosurs = 0
        removalsOpeners = 0
        openers = 0
        cleanedFromClosers = []
        for c in s:
            if c == "(":
                openers += 1
            elif c == ")":
                if openers > 0:
                    openers -= 1
                else:
                    removalsClosurs += 1
                    continue
            cleanedFromClosers.append(c)
        
        cleanedFromClosers.reverse()
        closers = 0
        
        for c in cleanedFromClosers:
            if c == ")":
                closers += 1
            elif c == "(":
                if closers > 0:
                    closers -= 1
                else:
                    removalsOpeners += 1
                    continue
        return (removalsOpeners, removalsClosurs)

sol = Solution()
# res = sol.removeInvalidParentheses("(()()")
# res = sol.removeInvalidParentheses("))(p(((())")
res = sol.removeInvalidParentheses("())v)(()(((((())")

print(res)
