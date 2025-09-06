# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        ans = []
        cols = set()
        posDiag = set()
        negDiag = set()

        def placeQueen(row, col):
            if row > n or col > n:
                return False

            if row == n:
                ans.append(self.buildBoard(n, queens))
                return True
            for nextCol in range(n):
                pd = row + nextCol
                nd = row - nextCol
                if pd in posDiag or nd in negDiag or nextCol in cols:
                    continue
                cols.add(nextCol)
                negDiag.add(nd)
                posDiag.add(pd)
                queens.append((row, nextCol))

                placeQueen(row + 1, col)
                
                negDiag.remove(nd)
                posDiag.remove(pd)
                cols.remove(nextCol)
                queens.pop()

            return False
        placeQueen(0, 0)
        return ans
            
    def buildBoard(self, n, queens):
        board = [["."] * n for _ in range(n)]
        for r, c in queens:
            board[r][c] = "Q"
            board[r] = ''.join(board[r])
        return board