# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        islands = 0
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1
                    queue = [(i, j)]
                    while queue:
                        r, c = queue.pop(0)
                        if grid[r][c] == "0":
                            continue
                        for xr, xc in dirs:
                            nr, nc = r + xr, c + xc
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1":
                                queue.append((nr, nc))
                        grid[r][c] = "0"

        return islands