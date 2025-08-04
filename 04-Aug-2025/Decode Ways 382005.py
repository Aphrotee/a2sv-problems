# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n + 1)

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] =dp[i + 1]

                if i + 1:
                    index = int(s[i:i+2])
                    if 10 <= index <= 26:
                        dp[i] += dp[i + 2]
        return dp[0]