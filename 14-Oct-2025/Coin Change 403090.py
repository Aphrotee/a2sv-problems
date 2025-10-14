# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        coins = set(coins)
        if amount == 0:
            return 0


        for amt in range(1, amount + 1):
            if amt in coins:
                dp[amt] = 1
            else:
                for coin in coins:
                    if coin < amt:
                        dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        return dp[amount] if dp[amount] < float("inf") else -1
