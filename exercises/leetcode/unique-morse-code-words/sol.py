from typing import List


morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_words = {}
        for word in words:
            morse_word = self.transformWordToMorse(word)
            unique_words[morse_word] = True
        return len(unique_words.keys())

    def transformWordToMorse(self, word: str) -> str:
        morse_chunks = []
        for c in word:
            idx = ord(c) - 97
            morse_seq = morse[idx]
            morse_chunks.append(morse_seq)
        return "".join(morse_chunks)

words = ["gin","zen","gig","msg"]
s = Solution()
res = s.uniqueMorseRepresentations(words)
# s.transformWordToMorse("b")
print(res)