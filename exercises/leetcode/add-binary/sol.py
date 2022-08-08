class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        if length > len(a):
            a = "0" * (length - len(a)) + a
        if length > len(b):
            b = "0" * (length - len(b)) + b
        
        final = []
        remainder = 0
        for ac, bc in zip(a[::-1], b[::-1]):
            if ac == "1":
                remainder += 1
            if bc == "1":
                remainder += 1
            
            if remainder == 0:
                final.append("0")
            elif remainder == 1:
                final.append("1")
                remainder = 0
            elif remainder == 2:
                final.append("0")
                remainder = 1
            else: # 3
                final.append("1")
                remainder = 1
            
        if remainder:
            final.append("1")
    
        return "".join(final[::-1])