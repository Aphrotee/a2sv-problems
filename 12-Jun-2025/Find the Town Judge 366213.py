# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        graph = [[0 for _ in range(n)] for _ in range(n)]

        for a, b in trust:
            graph[a - 1][b - 1] = 1

        potential = []
        for node, edges in enumerate(graph):
            if sum(edges) == 0:
                potential.append(node + 1)

        for judge in potential:
            target = True
            for person in range(n):
                if person != judge - 1:
                    if graph[person][judge - 1] == 0:
                        target = False
                        break
            if target:
                return judge
        return -1