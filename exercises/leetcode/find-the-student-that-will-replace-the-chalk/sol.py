class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        fullRoundUse = sum(chalk)
        leftUse = k % fullRoundUse

        for i in range(len(chalk)):
            curChalk = chalk[i]
            if curChalk > leftUse:
                return i

            leftUse -= curChalk
        
        return -1
