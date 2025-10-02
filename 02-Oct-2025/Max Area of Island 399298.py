# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])
        area = 0
        max_area = 0

        def dfs(row, col):
            nonlocal area
            if grid[row][col] == 0:
                return
            
            area += 1
            
            grid[row][col] = 0
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    dfs(nr, nc)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, area)
                    area = 0
        return max_area