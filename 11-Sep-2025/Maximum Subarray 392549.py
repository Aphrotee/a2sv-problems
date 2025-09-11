# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = 0
        max_sum = float("-inf")

        for num in nums:
            running_sum = max(0, running_sum) + num
            max_sum = max(running_sum, max_sum)
        return max(max_sum, running_sum)