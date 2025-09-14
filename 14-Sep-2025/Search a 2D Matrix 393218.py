# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.get_row(matrix, target)

        if row == -1:
            return False
        n = len(matrix[row])
        l, r = 0, n - 1

        while l < r:
            m = l + ((r - l) // 2)
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m
        if l == r and matrix[row][l] == target:
            return True

        return False
    
    def get_row(self, grid: List[List[int]], target: int) -> int:
        n = len(grid)
        u, d = 0, n - 1

        while u < d:
            m = u + ((d - u) // 2)
            if grid[m][0] <= target <= grid[m][-1]:
                return m
            elif target < grid[m][0]:
                d = m
            elif target > grid[m][0]:
                u = m + 1
        if u == d and grid[u][0] <= target <= grid[u][-1]:
            return u
        return -1


