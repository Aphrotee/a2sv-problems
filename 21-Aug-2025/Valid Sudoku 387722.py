# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])

        rows = [0] * 9
        cols = [0] * 9
        grid = defaultdict(int)

        for r in range(n):
            for c in range(m):
                cell = board[r][c]
                gr, gc = r // 3, c // 3
                if cell != ".":
                    cell_bit = 1 << int(cell)
                    if rows[r] & cell_bit != 0 or cols[c] & cell_bit != 0 or grid[(gr,gc)] & cell_bit != 0:
                        return False
                    else:
                        rows[r] |= cell_bit
                        cols[c] |= cell_bit
                        grid[(gr,gc)] |= cell_bit
        return True

