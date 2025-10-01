# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        downDiag = set() # c - r
        upDiag = set() # r + c
        columns = set()
        ans = []
        
        def placeQueen(row, queens):
            if row == n:
                ans.append(self.getQueens(n, queens))
                return
            for col in range(n):
                up =  row + col
                down = row - col
                if up not in upDiag and down not in downDiag and col not in columns:
                    upDiag.add(up)
                    downDiag.add(down)
                    columns.add(col)
                    queens.append((row, col))
                    placeQueen(row + 1, queens)
                    upDiag.remove(up)
                    downDiag.remove(down)
                    columns.remove(col)
                    queens.pop()
        placeQueen(0,  [])
        return ans
    def getQueens(self, size, queens):
        board = [["." for _ in range(size)] for _ in range(size)]
        for r,c in queens:
            board[r][c] = "Q"
            board[r] = ''.join(board[r])
        return board