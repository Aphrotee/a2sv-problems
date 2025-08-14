# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = [0] * (amount + 1)
        # dp[0] = 1


        
        # for c in coins:
        #     for a in range(c, amount + 1):
        #         if c <= a:
        #             dp[a] += dp[a - c]
        # return dp[amount]
        dp = defaultdict(int)
        n = len(coins)

        def change(index, amt):
            nonlocal n
            if index == n or amt > amount:
                if amt == amount:
                    return 1
                return 0
            if (index, amt) in dp:
                return dp[(index, amt)]
            
            dp[(index, amt)] += (change(index, amt + coins[index]) + change(index + 1, amt))
            return dp[(index, amt)]
        
        return change(0, 0)

