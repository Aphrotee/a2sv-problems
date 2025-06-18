# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)
        
        taken = set()
        visited = set()
        def dfs(course):
            if course in taken:
                return True  
            if course in visited:
                return False          
            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            taken.add(course)
            return True
        for courseId in range(numCourses):
            if not dfs(courseId):
                return False
        return True