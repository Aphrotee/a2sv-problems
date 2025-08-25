# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[float("inf") for _ in range(n + 2)] for _ in range(n + 1)]
        for i in range(n + 2):
            dp[0][i] = 0
        

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i - 1][j - 1] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])        
        return min(dp[n])