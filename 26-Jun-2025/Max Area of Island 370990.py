# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = [0]
        maxArea = 0
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        def depthFirstSearch(row, col):
            matrix[row][col] = 0
            count[0] += 1
            for dr, dc in dirs:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < rows and 0 <= newCol < cols and matrix[newRow][newCol]:
                    depthFirstSearch(newRow, newCol)
                    
            
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    count[0] = 0
                    depthFirstSearch(i, j)
                    maxArea = max(maxArea, count[0])
        return maxArea