# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])
        number_of_islands = 0

        def dfs(row, col):
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    dfs(nr, nc)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    number_of_islands += 1
                    dfs(r, c)
        return number_of_islands