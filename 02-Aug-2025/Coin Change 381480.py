# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        if amount == 0:
            return 0
        dp[0] = 0

        for a in range(amount + 1):
            if a in coins:
                dp[a] = 1
            else:
                for c in coins:
                    if c < a:
                        dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if isinstance(dp[amount], int) else -1