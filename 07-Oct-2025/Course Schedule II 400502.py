# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        taken = {}

        answer = []

        adj = defaultdict(list)
        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)

        def dfs(course):
            nonlocal answer
            if course in taken:
                if taken[course]:
                    return True
                else:
                    answer = []
                    return False
            taken[course] = False
            
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
                
            taken[course] = True
            answer.append(course)
            return True
        

        for c in range(numCourses):
            if c not in taken:
                if not dfs(c):
                    break
        return answer