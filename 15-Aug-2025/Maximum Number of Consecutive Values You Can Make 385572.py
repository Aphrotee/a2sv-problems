# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        last_max = 0
        for c in coins:
            if c - last_max > 1:
                return last_max + 1
            last_max += c
        return last_max + 1