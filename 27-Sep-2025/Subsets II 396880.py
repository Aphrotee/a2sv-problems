# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        def find_subset(index, current_subset):
            nonlocal n, ans
            if index == n:
                ans.append(current_subset[:])
                return
            current_subset.append(nums[index])
            find_subset(index + 1, current_subset)
            current_subset.pop()

            to_skip = nums[index]
            while index < n and nums[index] == to_skip:
                index += 1
            find_subset(index, current_subset)
        find_subset(0, [])
        return ans