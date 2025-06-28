# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: set() for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].add(prereq)
        taken = set()        
        
        def dfs(course, to_take):
            if course in to_take:
                return False
            if course in taken:
                return True
            to_take.add(course)
            taken.add(course)
            for pre in adj[course]:
                if pre not in to_take:
                    
                    if not dfs(pre, to_take):
                        return False
                elif pre not in taken:
                    continue
                else:
                    return False
            to_take.remove(course)
            return True

        for c, p in prerequisites:
            if c in taken:
                continue
            if not dfs(c, set()):
                return False
        return True