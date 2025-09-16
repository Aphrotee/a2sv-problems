# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZeros = set()
        colZeros = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowZeros.add(i)
                    colZeros.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in rowZeros or j in colZeros:
                    matrix[i][j] = 0