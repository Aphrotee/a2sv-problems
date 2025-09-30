# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])
        n = len(word)
        found = False
        def findWord(index, row, col):
            nonlocal found, n, rows, cols
            if index == n:
                found = True
                return
            if word[index] != board[row][col]:
                return
            if word[index] == board[row][col] and index == n - 1:
                found = True
                return
            char = board[row][col]
            board[row][col] = "#"
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    findWord(index + 1, nr, nc)
            board[row][col] = char
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    findWord(0, r, c)
        return found
            
            
