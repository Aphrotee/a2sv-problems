# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.hash = {} # {0: F, 1: F, 2: T, 5: T, 3: F}
        n = len(graph)
        def dfs(node):

            self.hash[node] = False
            
            for neighbour in graph[node]:
                if neighbour in self.hash:
                    if not self.hash[neighbour]:
                        return
                else:
                    dfs(neighbour)
            for neighbour in graph[node]:
                if self.hash[neighbour] == False:
                    return 
            self.hash[node] = True
        
        for node in range(n):
            if node not in self.hash:
                dfs(node)

        ans = []
        for node in range(n):
            if self.hash[node]:
                ans.append(node)

        return ans