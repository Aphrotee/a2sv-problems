# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.N = len(word)
        self.m = len(board)
        self.n = len(board[0])


        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        def search(index, current):
            if index == self.N:
                return True
            for d in dirs:
                r = current[0] + d[0]
                c = current[1] + d[1]
                if r < 0 or r >= self.m or c < 0 or c >= self.n:
                    continue
                temp = (r, c)   
                if board[r][c] == word[index] and temp not in path:
                    path.add(temp)
                    if search(index + 1, temp):
                        return True
                    path.remove(temp)
            return False
        path = set()
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    path.add((i, j))
                    if search(1, (i, j)):
                        return True
                    path.remove((i, j))
        return False