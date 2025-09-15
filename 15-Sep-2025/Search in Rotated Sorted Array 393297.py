# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m
        if l == r and nums[l] == target:
            return l
        return -1