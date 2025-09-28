# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:


        rows = len(matrix)
        if rows == 0:
            return True
        cols = len(matrix[0])

        for row in range(1, rows):
            for col in range(1, cols):
                prevRow = row - 1
                prevCol = col - 1
                if prevRow >= 0 and prevCol >= 0:
                    if matrix[row][col] != matrix[prevRow][prevCol]:
                        return False
        return True
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if not self.checkDiagonal(matrix, len(matrix), len(matrix[0]), i, j):
        #             return False
        # return True

    def checkDiagonal(self, matrix, rows, cols, r, c):
        dr, dc = r - 1, c - 1
        if 0 <= dr < rows and 0 <= dc < cols:
            if matrix[dr][dc] != matrix[r][c]:
                return False
        return True