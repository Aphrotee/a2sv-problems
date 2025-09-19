# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])
        cr, cc = click
        if board[cr][cc] == "M":
            board[cr][cc] = "X"
        else:
            queue = deque([(cr, cc)])
            seen = set()
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            while queue:
                r, c = queue.popleft()
                if (r, c) in seen:
                    continue
                seen.add((r, c))
                mines = 0

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == "M":
                            mines += 1
                board[r][c] = "B" if mines == 0 else str(mines)
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr, nc) not in seen and board[nr][nc] == "E" and board[r][c] == "B":
                            queue.append((nr, nc))
                
        return board