# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_area = 0
        

        def bfs(row, col):
            queue = deque([(row, col)])
            area = 0
            visited = set([(row, col)])
            while queue:
                r, c = queue.popleft()
                area += 1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        grid[r][c] = 0
            return area
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    grid[i][j] = 0
                    max_area = max(area, max_area)
        return max_area