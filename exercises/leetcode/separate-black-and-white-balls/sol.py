class Solution:
    def minimumSteps(self, s: str) -> int:
        zeroPos = 0
        walker = 0
        steps = 0

        while walker < len(s):
            if s[walker] == "0":
                steps += walker - zeroPos
                zeroPos += 1

            walker += 1
        
        return steps

        