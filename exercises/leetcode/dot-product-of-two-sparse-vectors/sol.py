class SparseVector:
    def __init__(self, nums: List[int]):
        self.mapped = {}
        for i, v in enumerate(nums):
            if v == 0:
                continue
            self.mapped[i] = v
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i in self.mapped:
            if i not in vec.mapped:
                continue
                
            total += self.mapped[i] * vec.mapped[i]
        
        return total