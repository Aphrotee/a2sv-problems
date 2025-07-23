# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        temp = [[-1 for _ in range(m)] for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]

        for r in range(n):
            for c in range(m):
                alive = 0
                dead = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        if board[nr][nc] == 1:
                            alive += 1
                        elif board[nr][nc] == 0:
                            dead += 1
                if board[r][c] == 1:
                    if alive < 2 or alive > 3:
                        temp[r][c] = 0
                    else:
                        temp[r][c] = board[r][c]
                elif board[r][c] == 0:
                    if alive == 3:
                        temp[r][c] = 1
                    else:
                        temp[r][c] = board[r][c]
        for r in range(n):
            for c in range(m):
                board[r][c] = temp[r][c]