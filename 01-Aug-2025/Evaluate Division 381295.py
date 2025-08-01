# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(set)

        for i, pair in enumerate(equations):
            a, b = pair
            adj[a].add((b, values[i]))
            adj[b].add((a, 1 / values[i]))

        answer = []

        def bfs(x, y):
            if x not in adj or y not in adj:
                return -1
            if x == y:
                return 1
            queue = deque([(x, 1)])
            visited = set()
            while queue:
                var, val = queue.popleft()

                if var == y:
                    return val
                visited.add(var)
                for b, value in adj[var]:
                    if b not in visited:
                        queue.append((b, val * value))
            return -1

        for x, y in queries:
            answer.append(bfs(x, y))
        return answer