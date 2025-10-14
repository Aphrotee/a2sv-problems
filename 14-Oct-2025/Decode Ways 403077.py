# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            num1 = s[i - 1:i]
            
            if num1 != "0":
                dp[i] += dp[i - 1]
            if i - 2 >= 0:
                num2 = s[i - 2:i] 
                if 10 <= int(num2) <= 26:
                    dp[i] += dp[i - 2]
        return dp[n]