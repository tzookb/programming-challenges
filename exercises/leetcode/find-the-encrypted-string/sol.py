class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        res = []

        chars = list(s)
        for i in range(len(chars)):
            res.append(chars[(i + k) % len(chars)])
        
        return "".join(res)

        