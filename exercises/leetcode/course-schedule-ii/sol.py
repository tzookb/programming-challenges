from typing import List
from collections import defaultdict, deque, Counter
class Solution:

    def findOrder(self, numCourses, prerequisites):
        # Prepare the graph
        adj_list = defaultdict(list)
        deps_count = [0] * numCourses

        for dest_course, prev_course in prerequisites:
            adj_list[prev_course].append(dest_course)
            deps_count[dest_course] += 1

        ready_courses = []

        for course, count in enumerate(deps_count):
            if count == 0:
                ready_courses.append(course)

        ordering = []

        while ready_courses:
            cr = ready_courses.pop(0)
            ordering.append(cr)
            dependents = adj_list[cr]

            for depd in dependents:
                deps_count[depd] -= 1
                if deps_count[depd] == 0:
                    ready_courses.append(depd)

        if numCourses != len(ordering):
            return []

        return ordering

s = Solution()
numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
res = s.findOrder(numCourses, prerequisites)
# print(res)