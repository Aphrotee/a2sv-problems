# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        queue = []
        height = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
        visited = set()

        while queue:
            r, c, h = queue.pop(0)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            height[r][c] = h
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    queue.append((nr, nc, h + 1))
        return height