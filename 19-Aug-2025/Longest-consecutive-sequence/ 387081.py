# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                temp = num
                length = 0
                while temp in num_set:
                    temp += 1
                    length += 1
                max_length = max(length, max_length)
        return max_length