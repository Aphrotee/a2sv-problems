# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            s1 = s[i - 1:i]
            s2 = ""
            if i > 1:
                s2 = s[i - 2:i]
                if s2[0] == "0":
                    s2 = ""
            n1 = int(s1)
            n2 = int(s2) if s2 else 0
            if 1 <= n1 <= 9:
                dp[i] += dp[i - 1]
            if 10 <= n2 <= 26:
                dp[i] += dp[i - 2]
        return dp[n]