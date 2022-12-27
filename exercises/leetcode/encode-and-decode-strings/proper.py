from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        connect = []
        for str in strs:
            size = hex(len(str))[2:]
            size = size if len(size) == 4 else ("0" * (4 - len(size)) + size)
            connect.append(size)
            connect.append(str)
        
        return "".join(connect)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        cur = 3
        while cur < len(s):
            sizehex = s[cur - 3: cur + 1]
            size = int(sizehex,16)
            if size == 0:
                cur_str = ""
            else:
                cur_str = s[cur + 1 : cur + 1 + size]
            cur += size + 4
            result.append(cur_str)

        return result
        
# Your Codec object will be instantiated and called as such:
strs = ["123", "12345"]
strs = ["", "1234"]
codec = Codec()
encoded = codec.encode(strs)
decoded = codec.decode(encoded)
print(decoded)