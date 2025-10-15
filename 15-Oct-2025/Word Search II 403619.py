# Problem: Word Search II - https://leetcode.com/problems/word-search-ii/description/

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = {}
    
    def addWord(self, word, index):
        if index == len(word):
            return
        char = word[index]
        if char in self.children:
            node = self.children[char]
        else:
            node = TrieNode(char)
            self.children[char] = node
        node.addWord(word, index + 1)
        if index == len(word) - 1:
            node.end = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode('')

        for word in words:
            self.root.addWord(word, 0)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])
        n = len(word)
        found = set()
        def findWord(word, row, col, curr):
            nonlocal n, rows, cols
            word.append(curr.char)
            if curr.end:
                found.add(''.join(word))
            
            if curr.children:
                char = board[row][col]
                board[row][col] = "#"
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                        if board[nr][nc] in curr.children:
                            findWord(word, nr, nc, curr.children[board[nr][nc]])
                board[row][col] = char
            word.pop()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in self.root.children:
                    findWord([], r, c, self.root.children[board[r][c]])
        return list(found)
            
        