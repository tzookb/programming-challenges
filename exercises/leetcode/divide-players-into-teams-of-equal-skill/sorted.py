class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        teamscnt = len(skill) // 2
        target = total // teamscnt
        if total % teamscnt != 0:
            return -1

        skill.sort()
        
        last = len(skill) - 1
        pairs = []

        for i in range(last//2 + 1):
            small = skill[i]
            big = skill[last - i]
            if small + big != target:
                return -1
            pairs.append([small, big])

        
        return sum([pair[0] * pair[1] for pair in pairs])
        
        