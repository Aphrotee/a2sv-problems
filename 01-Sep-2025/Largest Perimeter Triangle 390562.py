# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_peri = 0
        for i in range(n - 2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                max_peri = max(max_peri, nums[i] + nums[i + 1] + nums[i + 2])
        return max_peri