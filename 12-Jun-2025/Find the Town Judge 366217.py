# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        graph = [[0, 0] for _ in range(n)]

        for a, b in trust:
            graph[b - 1][0] += 1
            graph[a - 1][1] += 1
        for node, degree in enumerate(graph):
            if degree[0] == n - 1 and degree[1] == 0:
                return node + 1
        return -1