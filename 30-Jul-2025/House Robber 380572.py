# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] + nums.copy()

        for i in range(len(memo)):
            if i > 1:
                memo[i] = max(memo[i - 1], memo[i] + memo[i - 2]) 

        return memo[-1]