# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        m = len(board)
        n = len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            visited.add((row, col))
            board[row][col] = "#"
            for r, c in dirs:
                newRow, newCol = row + r, col + c
                if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n:
                    if (newRow, newCol) not in visited and board[newRow][newCol] == "O":
                        dfs(newRow, newCol)

        for i in range(m):
            r, c1, c2 = i, 0, n - 1
            if (r, c1) not in visited and board[r][c1] == "O":
                dfs(r, c1)
            if (r, c2) not in visited and board[r][c2] == "O":
                dfs(r, c2)
        for j in range(n):
            r1, r2, c = 0, m - 1, j
            if (r1, c) not in visited and board[r1][c] == "O":
                dfs(r1, c)
            if (r2, c) not in visited and board[r2][c] == "O":
                dfs(r2, c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
