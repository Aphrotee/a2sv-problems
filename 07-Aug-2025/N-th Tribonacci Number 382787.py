# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        self.memo = {0: 0, 1: 1, 2: 1}
        return self.trib(n)

    def trib(self, n):
        if n in self.memo:
            return self.memo[n]
        
        val = self.trib(n - 1) + self.trib(n - 2) + self.trib(n - 3)
        self.memo[n] = val
        return val