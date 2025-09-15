# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] < nums[(m + 1) % n] and nums[m] < nums[m - 1]:
                return nums[m]
            elif nums[m] >= nums[-1] or (nums[m] > nums[r] and nums[m] > nums[l]):
                l = m + 1
            elif nums[m] <= nums[0] or nums[l] < nums[m] < nums[r]:
                r = m
        if l == r and nums[l] <= nums[(l + 1) % n] and nums[l] <= nums[l - 1]:
            return nums[l]
        return -1