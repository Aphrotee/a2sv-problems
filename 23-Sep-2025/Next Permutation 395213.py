# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        piv = n - 1

        while piv > 0 and nums[piv] <= nums[piv - 1]:
            piv -= 1
    
        start = piv
        if piv > 0:
            toSwap = n - 1
            while toSwap > 0 and nums[toSwap] <= nums[piv - 1]:
                toSwap -= 1
            nums[toSwap], nums[piv - 1] = nums[piv - 1], nums[toSwap]
        end = n - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1