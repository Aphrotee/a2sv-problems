# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:

    def find(self, node):
        parent = self.parent[node]
        if parent == node:
            return node
        self.parent[node] = self.find(parent)
        return self.parent[node]
    
    def union(self, x, y):
        xParent = self.find(x)
        yParent = self.find(y)

        if xParent == yParent:
            return 0
        if self.rank[xParent] < self.rank[yParent]:
            xParent, yParent = yParent, xParent
        
        self.parent[yParent]= xParent
        self.rank[xParent] += self.rank[yParent]

        return 1

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        stones.sort()
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

        xMap = {}
        yMap = {}
        removed = 0

        for i, (x, y) in enumerate(stones):
            if x in xMap:
                removed += self.union(xMap[x], i)
            else:
                xMap[x] = i
            if y in yMap:
                removed += self.union(yMap[y], i)
            else:
                yMap[y] = i
        return removed