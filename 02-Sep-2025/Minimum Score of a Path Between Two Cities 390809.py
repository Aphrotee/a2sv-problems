# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.minWeight = float("inf")

        self.adj = defaultdict(set)
        for a, b, d in roads:
            self.adj[a].add((b, d))
            self.adj[b].add((a, d))
        self.seen = set()
        def dfs(node):
            if node in self.seen:
                return
            self.seen.add(node)
            for neighb, weight in self.adj[node]:
                self.minWeight = min(self.minWeight, weight)
                if neighb not in self.seen:
                    dfs(neighb)
        dfs(1)
        return self.minWeight