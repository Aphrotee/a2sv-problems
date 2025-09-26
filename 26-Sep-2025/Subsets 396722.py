# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i, current_subset):
            nonlocal ans
            if i == len(nums):
                ans.append(current_subset[:])
                return
            current_subset.append(nums[i])
            backtrack(i+1, current_subset)
            current_subset.pop()
            backtrack(i+1, current_subset)
        backtrack(0, [])
        return ans