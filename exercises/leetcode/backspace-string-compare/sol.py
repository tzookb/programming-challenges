class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_typed_char_reveresed(typing: str):
            skips = 0
            for c in typing[::-1]:
                if c == "#":
                    skips += 1
                elif skips:
                    skips -= 1
                else:
                    yield c
        
        s_chars = get_typed_char_reveresed(s)
        t_chars = get_typed_char_reveresed(t)
        
        for s_c, t_c in itertools.zip_longest(s_chars, t_chars):
            if s_c != t_c:
                return False

        return True
