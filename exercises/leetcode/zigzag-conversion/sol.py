class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        in_lines = [""] * numRows
        

        line = 1
        direction = 1
        for c in s:
            in_lines[line - 1] += c
            
            line += direction
            if line == numRows:
                direction = -1
            if line == 1:
                direction = 1
        
        
        return "".join(in_lines)
