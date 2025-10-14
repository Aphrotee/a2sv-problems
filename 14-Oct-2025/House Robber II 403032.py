# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * (n)
        dp2 = [0] * (n)
        if len(nums) <= 2:
            return max(nums)

        for house in range(1, n):
            dp1[house] = max(nums[house - 1] + dp1[house - 2], dp1[house - 1])
        nums.reverse()
        for house in range(1, n):
            dp2[house] = max(nums[house - 1] + dp2[house - 2], dp2[house - 1])

        return max(dp1[n - 1], dp2[n - 1])