class Solution:
    def convertDateToBinary(self, date: str) -> str:
        chunks = date.split("-")
        parts = [self.getBinary(int(chunk)) for chunk in chunks]
        return "-".join(parts)

    def getBinary(self, num: int) -> str:
        return format(num, 'b')
