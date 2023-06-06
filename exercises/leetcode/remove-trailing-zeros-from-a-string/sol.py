class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        resp = []
        skipped = False

        for c in num[::-1]:
            if skipped:
                resp.append(c)
                continue
            
            if c != "0":
                skipped = True
                resp.append(c)
                continue
        
        return "".join(resp[::-1])