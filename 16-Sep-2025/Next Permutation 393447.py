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
            nextIndex = n - 1
            while nextIndex >= 0:
                if nums[piv - 1] < nums[nextIndex]:
                    nums[nextIndex], nums[piv - 1] = nums[piv - 1], nums[nextIndex]
                    break
                nextIndex -= 1

        l, r = start, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1