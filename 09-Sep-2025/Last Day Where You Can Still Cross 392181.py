# Problem: Last Day Where You Can Still Cross - https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        area = [[0 for _ in range(col)] for _ in range(row)]
        days = len(cells)
        ans = 0
        l, r = 0, days - 1

        while l < r:
            m = l + ((r - l) // 2)
            waters = self.getWaters(cells, m + 1)
            can_cross = self.pathExists(row, col, waters)

            if can_cross:
                ans = max(ans, m + 1)
                l = m + 1
            else:
                r = m
        return ans
    
    def pathExists(self, rows: int, cols: int, waters: set) -> bool:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = self.getStarts(cols, waters)

        seen = set(queue)

        while queue:
            r, c = queue.popleft()
            if r == rows:
                return True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 1 <= nr <= rows and 1 <= nc <= cols and (nr, nc) not in seen and (nr, nc) not in waters:
                    queue.append((nr, nc))
                    seen.add((nr, nc))
        return False


    def getWaters(self, cells, day):
        ans = set()
        for d in range(day):
            r, c = cells[d]
            ans.add((r, c))
        return ans
    
    def getStarts(self, cols: int, waters: set):
        starts = deque()
        for c in range(1, cols + 1):
            start = (1, c)
            if start not in waters:
                starts.append(start)
        return starts