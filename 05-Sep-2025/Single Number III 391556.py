# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = set(nums)
        n = len(nums)
        x = 0
        N = len(nums)
        for num in nums:
            x ^= num
        
        mask = 1

        while not(x & mask):
            mask <<= 1
        
        a, b = 0, 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
            

