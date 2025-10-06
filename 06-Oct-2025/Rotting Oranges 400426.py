# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        min_time = 0
        seen = set()
        while queue:
            r, c, m = queue.popleft()
            if (r, c) in seen:
                continue
            seen.add((r, c))
            grid[r][c] = 2
            min_time = max(min_time, m)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in seen:
                    queue.append((nr, nc, m + 1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return min_time