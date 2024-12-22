class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedDict = {}
        for word in bannedWords:
            bannedDict[word] = True
        
        counted = 0
        for word in message:
            if word in bannedDict:
                counted += 1
                if counted == 2:
                    return True
        return False
