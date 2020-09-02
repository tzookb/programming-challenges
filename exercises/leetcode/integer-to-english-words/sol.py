class Solution:
    def __init__(self):
        self.singles = { 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 0: ""}
        self.tenSingles = { 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 10: "Ten"}
        self.tens = { 1: "Ten", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety", 10: ""}
        self.jumps = ["", "Thousand", "Million", "Billion"]

    def single(self, num: int) -> str:
        return self.singles[num]
    
    def pair(self, num: int) -> str:
        if num < 10:
            return self.single(num)
        if 10 < num < 20:
            return self.tenSingles[num]
        ten = self.tens[num//10]
        single = self.single(num%10)
        return f"{ten} {single}"

    def trio(self, num: int) -> str:
        houndredDigit = num // 100
        tensLeft = num % 100
        final = []
        if houndredDigit:
            final.append(self.single(houndredDigit) + " Hundred")
        tensLeftStr = self.pair(tensLeft)
        if tensLeftStr != "":
            final.append(tensLeftStr)
        return (" ".join(final)).strip()

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        final = []
        curJump = 0
        prevNum = None
        while num:
            curNum = num % 1000
            num //= 1000

            curNumStr = self.trio(curNum)
            curFinal = [curNumStr]
            jusmPhrase = self.jumps[curJump]
            if jusmPhrase != "" and curNumStr != "":
                curFinal.append(jusmPhrase)
            curJump += 1
            final.append(" ".join(curFinal))

        final = list(filter(lambda x: x!="", final))

        return (" ".join(final[::-1])).strip()


s = Solution()
res = s.numberToWords(1000010)
print(res)