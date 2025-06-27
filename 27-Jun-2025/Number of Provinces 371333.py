# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].add(j)
                    adj[j].add(i)
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            
            for nextNode in adj[node]:
                if nextNode not in visited:
                    dfs(nextNode)
        provinces = 0
        for i in range(n):
            if i not in visited:
                provinces += 1
                dfs(i)
        return provinces
