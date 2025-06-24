# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        answer = [float("inf")] * n
        redAdj = [set() for _ in range(n)]
        blueAdj = [set() for _ in range(n)]

        for src, dest in redEdges:
            redAdj[src].add(dest)

        for src, dest in blueEdges:
            blueAdj[src].add(dest)
        

        queue = [(0, "b", 0), (0, "r", 0)]
        redVisited = set()
        blueVisited = set()
        while queue:
            node, colour, distance = queue.pop(0)

            for dest in range(n):
                if node == dest:
                    answer[dest] = min(distance, answer[dest])
                    break

            if colour == "r":
                redVisited.add(node)
            elif colour == "b":
                blueVisited.add(node)

            if colour == "b":
                for nextNode in redAdj[node]:
                    if nextNode not in redVisited:
                        queue.append((nextNode, "r", distance + 1))
            elif colour == "r":
                for nextNode in blueAdj[node]:
                    if nextNode not in blueVisited:
                        queue.append((nextNode, "b", distance + 1))
        
        for i, dist in enumerate(answer):
            if not dist < float("inf"):
                answer[i] = -1
        return answer