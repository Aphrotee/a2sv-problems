# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for num in nums:
            index = abs(num) - 1
            if index < n and nums[index] > 0:
                nums[index] = -nums[index]
        for potential in range(1, n + 1):
            if nums[potential - 1] > 0:
                return potential
        return n + 1