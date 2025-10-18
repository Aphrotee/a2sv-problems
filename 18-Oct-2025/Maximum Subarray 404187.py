# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum