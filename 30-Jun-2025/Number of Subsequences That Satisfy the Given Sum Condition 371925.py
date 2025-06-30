# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        left, right = 0, size - 1

        count = 0
        mod = (10 ** 9) + 7

        while left <= right:
            if nums[left] + nums[right] <= target:
                count += ((2 ** (right - left))) % mod
                left += 1
            else:
                right -= 1
        return count % mod