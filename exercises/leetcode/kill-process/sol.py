from typing import List, Optional
# Definition for a binary tree node.
class Solution:

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parents_kids_map = {}

        for pid_idx, parent  in enumerate(ppid):
            pidname = pid[pid_idx]
            if parent not in parents_kids_map:
                parents_kids_map[parent] = set()
            parents_kids_map[parent].add(pidname)
        
        kills = set([kill])
        nexts = list(parents_kids_map[kill]) if kill in parents_kids_map else []

        while nexts:
            cur = nexts.pop()
            kills.add(cur)
            if cur not in parents_kids_map:
                continue
            nexts += parents_kids_map[cur]
        
        return kills