# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = set(nums)
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                ans.remove(nums[i])
        return list(ans)