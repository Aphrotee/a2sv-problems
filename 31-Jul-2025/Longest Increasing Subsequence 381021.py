# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        lis = [1] * n
        longest = 0
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])
            longest = max(longest, lis[i])
        return longest
