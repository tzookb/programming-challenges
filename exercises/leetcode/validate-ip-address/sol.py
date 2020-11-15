class Solution:
    def validIPv4Part(self, part: str) -> bool:
        if len(part) > 3 or len(part) == 0:
            return False
        if part[0] == "0" and len(part) > 1:
            return False
        try:
            num = int(part)
        except:
            return False
        if num < 0 or num > 255:
            return False
        return True

    def validIPv4(self, IP: str) -> bool:
        parts = IP.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not self.validIPv4Part(part):
                return False
        return True
        
    def validIPv6Part(self, part: str) -> bool:
        if len(part) > 4 or len(part) == 0:
            return False
        part= part.upper()
        for c in part:
            v = ord(c)
            if 57 >= v >= 48 or 70 >= v >= 65:
                continue
            else:
                return False
        return True

    def validIPv6(self, IP: str) -> bool:
        parts = IP.split(":")
        if len(parts) != 8:
            return False
        for part in parts:
            if not self.validIPv6Part(part):
                return False
        return True

    def validIPAddress(self, IP: str) -> str:
        if self.validIPv4(IP):
            return "IPv4"
        if self.validIPv6(IP):
            return "IPv6"
        return "Neither"

p = "20EE:FGb8:85a3:0:0:8A2E:0370:7334"
s = Solution()
res = s.validIPAddress(p)
# res = s.validIPv6Part('FGb8')
print(res)