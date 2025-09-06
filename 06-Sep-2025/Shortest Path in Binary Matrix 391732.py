# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 1)])
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return -1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1), (1, 1)]
        while queue:
            row, col, pathLength = queue.popleft()

            if (row, col) == (n - 1, m - 1):
                return pathLength
            for dr, dc in dirs:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < n and 0 <= newCol < m and grid[newRow][newCol] == 0:
                    grid[newRow][newCol] = 1
                    queue.append((newRow, newCol, pathLength + 1))
        return -1