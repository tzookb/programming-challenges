from typing import List
class Solution:
    def justifyLine(self, words: List[str], maxWidth: int) -> str:
        words_count = len(words)
        space_by_words = sum([len(w) for w in words])
        if words_count == 1:
            return words[0] + " " * (maxWidth - space_by_words)
        total_holes = words_count - 1
        left_space = maxWidth - space_by_words
        hole_size = left_space // total_holes
        prefix = left_space - hole_size * total_holes

        final_arr = []
        for i in range(len(words)):
            final_arr.append(words[i])
            final_arr.append(" "*hole_size)
            if prefix > 0:
                final_arr.append(" ")
                prefix -= 1
        final_arr.pop()

        return  "".join(final_arr)

    def handleLastLine(self, words: List[str], maxWidth: int) -> str:
        words_count = len(words)
        space_by_words = sum([len(w) for w in words])
        only_words = " ".join(words)
        return only_words + " " * (maxWidth - len(only_words))

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        splitted_lines = []
        cur_line = []
        cur_size = 0
        for word in words:
            spaces_count = len(cur_line)
            total_size = spaces_count + cur_size
            new_word_len = len(word)
            total_size_with_new = total_size + new_word_len
            if total_size_with_new <= maxWidth:
                cur_size += new_word_len
                cur_line.append(word)
            else:
                splitted_lines.append(cur_line)
                cur_line = [word]
                cur_size = new_word_len

        if cur_line:
            splitted_lines.append(cur_line)

        final = []
        last_idx = len(splitted_lines) - 1
        for idx, words in enumerate(splitted_lines):
            if idx == last_idx:
                res = self.handleLastLine(words, maxWidth)
            else:
                res = self.justifyLine(words, maxWidth)
            final.append(res)

        return final


s = Solution()


# res = s.fullJustify(
#     ["What","must","be","acknowledgment","shall","be"],
#     16
# )
res = s.justifyLine(
    ["example","of","text"],
    16
)

print([res])