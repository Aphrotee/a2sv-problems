# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class DSU:
    def __init__(self, n):
        self.parents = {i: i for i in range(1, n + 1)}
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        parentX = self.parents[x]
        if x == parentX:
            return x
        return self.find(parentX)
    
    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)

        if parX == parY:
            return False
        
        if self.rank[parX] >= self.rank[parY]:
            self.parents[parY] = parX
            self.rank[parX] += self.rank[parY]
        else:
            self.parents[parX] = parY
            self.rank[parY] += self.rank[parX]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)

        for src, dest in edges:
            if not dsu.union(src, dest):
                return [src, dest]
