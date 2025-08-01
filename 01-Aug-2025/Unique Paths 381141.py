# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def __init__(self):
        self.memo = {0 : 1, 1: 1}

    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.comb(m  + n - 2, n - 1))
     
    def comb(self, n: int, r: int) -> int:
        return self.factorial(n) / (self.factorial(n - r) * self.factorial(r))
    
    def factorial(self, num: int) -> int:
        if num in self.memo:
            return self.memo[num]
        
        value = num * self.factorial(num - 1)
        self.memo[num] = value
        return value
