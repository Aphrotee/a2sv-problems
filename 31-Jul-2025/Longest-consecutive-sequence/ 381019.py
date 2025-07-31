# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        candidates = set()
        for num in nums:
            if num - 1 not in hashset:
                candidates.add(num)
        for num in candidates:
            count = 0
            consec_num = num
            while consec_num in hashset:
                count += 1
                consec_num += 1
            longest = max(longest, count)
        return longest