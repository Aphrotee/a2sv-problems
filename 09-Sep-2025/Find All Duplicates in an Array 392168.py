# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set(nums)
        for num in nums:
            if num in ans:
                ans.remove(num)
            else:
                ans.add(num)
        return list(ans)