# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        
        for factor in range(1, n + 1):
            if n % factor == 0:
                count += 1
                if count == k:
                    return factor
        return -1