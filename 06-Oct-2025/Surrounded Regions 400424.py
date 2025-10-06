# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()

        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            if board[r][0] == "O":
                queue.append((r, 0))
            if board[r][cols - 1] == "O":
                queue.append((r, cols - 1))
        
        for c in range(cols):
            if board[0][c] == "O":
                queue.append((0, c))
            if board[rows - 1][c] == "O":
                queue.append((rows - 1, c))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            board[r][c] = "Y"

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "Y":
                    board[r][c] = "O"