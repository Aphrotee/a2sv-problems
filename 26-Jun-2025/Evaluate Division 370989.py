# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for equation, value in zip(equations, values):
            adj[equation[0]].append((equation[1], value)) # a: (b, 2)
            adj[equation[1]].append((equation[0], 1 /value)) # b: (a, 0.5)
        
        def dfs(source, target, value):
            visited.add(source)

            if source not in adj or target not in adj:
                return -1
            if source == target:
                return value
            
            for neighbour, val in adj[source]:
                if neighbour not in visited:
                    answer = dfs(neighbour, target, value * val)
                    if answer != -1:
                        return answer
            return -1

        for i, query in enumerate(queries):
            visited = set()
            queries[i] = dfs(query[0], query[1], 1)
        
        return queries