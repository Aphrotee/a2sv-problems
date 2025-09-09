# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                ans.append(abs(num))
            nums[index] = -nums[index]
        return ans