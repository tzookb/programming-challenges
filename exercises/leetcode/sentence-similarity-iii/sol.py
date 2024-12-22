class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split(" ")
        w2 = sentence2.split(" ")
        if len(w1) == len(w2):
            return sentence1 == sentence2
        
        if len(w1) > len(w2):
            small = w2
            big = w1
        else:
            small = w1
            big = w2
        
        if not small:
            return True
        
        diff = len(big) - len(small)

        if small[0] != big[0]:
            leftbig = big[diff:]
            return small == leftbig
        
        if small[-1] != big[-1]:
            leftbig = big[0:-diff]
            return small == leftbig

        for i in range(len(small)):
            if big[i] != small[i]:
                break

        bigi = i + diff

        while i < len(small):
            if big[bigi] != small[i]:
                return False
            bigi += 1
            i += 1

        return True
            