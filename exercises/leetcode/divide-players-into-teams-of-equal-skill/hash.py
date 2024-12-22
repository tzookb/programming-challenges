class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        teamscnt = len(skill) // 2

        if total % teamscnt != 0:
            return -1
        
        goal = total // teamscnt

        partners = Counter()
        pairs = []

        for sk in skill:
            possible = goal - sk
            if possible in partners:
                partners[possible] -= 1
                if partners[possible] == 0:
                    del partners[possible]

                pairs.append([possible, sk])
            else:
                partners[sk] += 1
        
        if partners:
            return -1
        
        
        return sum([pair[0] * pair[1] for pair in pairs])
        
        