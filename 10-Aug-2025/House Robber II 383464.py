# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        gain1, gain2 = 0, 0
        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)
        i = 2
        if n == 1:
            return nums[0]
        elif n == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        while i < n + 1:
            dp1[i] = max(dp1[i - 1], nums[i - 1] + dp1[i - 2])
            dp2[i] = max(dp2[i - 1], nums[i - 2] + dp2[i - 2])
            i += 1
        return max(dp1[n], dp2[n])