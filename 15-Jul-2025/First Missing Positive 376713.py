# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for i, num in enumerate(nums):
            idx = abs(num) - 1
            if not 0 <= idx <= n - 1: continue
            if nums[idx] > 0:
                nums[idx] *= -1
            elif nums[idx] == 0:
                nums[idx] = -(n + 1)
        
        for k in range(1, n + 1):
            idx = k - 1
            if nums[idx] >= 0:
                return k
        return n + 1