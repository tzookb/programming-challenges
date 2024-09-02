class Solution:
    def pathSum(self, nums: List[int]) -> int:
        head = self.getHead(nums)
        totalPaths = 0

        dfs = [(head, 0)]
        
        while dfs:
            curNode, curPathSum = dfs.pop()
            if not curNode:
                continue

            pathHere = curPathSum + self.extractValue(curNode)
            childs = self.getChildren(curNode, nums)

            if not childs:
                totalPaths += pathHere
                continue
            
            for child in childs:
                curChildVal = self.extractValue(child)
                dfs.append((child, pathHere))
        
        return totalPaths
    
    def getHead(self, nums: List[int]) -> int:
        for num in nums:
            if num < 200:
                return num
        raise "error"

    def extractValue(self, num: int) -> int:
        return num % 10

    def getChildren(self, cur: int, nums: List[int]) -> List[int]:
        level = cur // 100
        childLevel = level + 1
        position = (cur % 100) // 10
        leftchild = (childLevel * 100 + (position * 2 - 1)*10)/10
        rightchild = (childLevel * 100 + (position * 2)*10)/10

        returnedChilds = []

        for num in nums:
            if num//10 == leftchild:
                returnedChilds.append(num)
            if num//10 == rightchild:
                returnedChilds.append(num)

        return returnedChilds