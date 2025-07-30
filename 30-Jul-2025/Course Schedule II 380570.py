# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(set)

        for a, b in prerequisites:
            adj[a].add(b)
        
        self.ordering = []
        self.taken = {}
        def dfs(node):
            self.taken[node] = False
            for p in adj[node]:
                if p not in self.taken:
                    if not dfs(p):
                        return False
                else:
                    if self.taken[p]:
                        continue
                    else:
                        return False
            self.taken[node] = True
            self.ordering.append(node)
            return True
        for course in range(numCourses):
            if course not in self.taken:
                if not dfs(course):
                    return []
        return self.ordering