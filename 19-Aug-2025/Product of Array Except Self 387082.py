# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        suff = [1] * n
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                suff[i] = suff[i + 1] * nums[i + 1]
        
        pref = 1
        for i in range(n):
            temp = pref * nums[i]
            nums[i] = pref * suff[i]
            pref = temp
        return nums