# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        need = {"u": "d", "d": "u", "l": "r", "r": "l"}
        dirs = {"l": (0, -1), "u": (-1, 0), "r": (0, 1), "d": (1, 0)}
        streets = {1: "lr", 2: "ud", 3: "ld", 4: "rd", 5: "ul", 6: "ur"}

        queue = [(0, 0)]
        visited = set()

        while queue:
            r, c = queue.pop(0)
            street = streets[grid[r][c]]
            if (r, c) == (rows - 1, cols - 1):
                return True
            if (r, c) in visited:
                continue
            visited.add((r, c))

            for edge in street:
                dr, dc = dirs[edge]
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    nextStreet = streets[grid[nr][nc]]
                    if need[edge] in nextStreet:
                        queue.append((nr, nc))
        return False