# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()

        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)
            
            for neigh in adj[node]:
                if dfs(neigh):
                    return True
            return False
        
        return dfs(source)