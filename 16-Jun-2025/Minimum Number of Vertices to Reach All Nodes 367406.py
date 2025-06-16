# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degrees = [0] * n

        for x, y in edges:
            degrees[y] += 1
        answer = []
        for node, deg in enumerate(degrees):
            if deg == 0:
                answer.append(node)
        return answer