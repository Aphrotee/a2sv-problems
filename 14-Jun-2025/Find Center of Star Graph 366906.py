# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = defaultdict(int)
        store = set()

        for a, b in edges:
            # n = max(a, b, n)
            # degree[a] += 1
            # degree[b] += 1
            if a in store:
                return a
            elif b in store:
                return b
            store.add(a)
            store.add(b)
        
        # for node, deg in degree.items():
        #     if deg == n - 1:
        #         return node
        