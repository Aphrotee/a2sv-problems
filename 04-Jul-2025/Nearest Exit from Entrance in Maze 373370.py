# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        queue = [(entrance[0], entrance[1], 0)]
        while queue:

            r, c, d = queue.pop(0)
            
            if maze[r][c] != ".":
                continue
            
            if (0 == r or r == m - 1 or 0 == c or c == n - 1) and (r, c) != tuple(entrance):
                return d
            maze[r][c] = "#"
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                    queue.append((nr, nc, d + 1))
        return -1
