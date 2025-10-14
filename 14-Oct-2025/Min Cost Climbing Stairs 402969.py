# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [float("inf")] * (n + 1)
        dp[0] = dp[1] = 0

        # [10, 15, 20]
        # [ 0,  0, 10, 0]

        for step in range(n):
            dp[step + 1] = min(dp[step + 1], cost[step] + dp[step])
            if step + 2 < n + 1:
                dp[step + 2] = min(dp[step + 2], cost[step] + dp[step])
        
        return dp[n]