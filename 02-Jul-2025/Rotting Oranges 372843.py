# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        n = len(grid)
        m = len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        visited = set()
        time_taken = 0
        while queue:
            r, c, time = queue.pop(0)

            if (r, c) in visited:
                continue
            visited.add((r, c))
            if grid[r][c] == 1:
                grid[r][c] += 1
            time_taken = max(time_taken, time)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    queue.append((nr, nc, time + 1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return time_taken