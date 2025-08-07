# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1

        dp = [0] * (n + 1)
        dp[1] = cost[0]
        dp[2] = cost[1]
        cost.append(0)

        for i in range(3, n + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])
        return dp[n]
