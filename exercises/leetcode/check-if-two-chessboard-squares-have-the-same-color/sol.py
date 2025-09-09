class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def colType(col):
            idx = ord(col) - ord("a") + 1
            return "b" if idx % 2 == 1 else "w"
        
        def getSquareCal(rowid, colType):
            even = rowid % 2 == 0
            if colType == "b":
                return "white" if even else "black"
            
            return "black" if even else "white"
        
        f = getSquareCal(int(coordinate1[1]), colType(coordinate1[0]))
        s = getSquareCal(int(coordinate2[1]), colType(coordinate2[0]))
        return f == s
            

        