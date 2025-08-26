# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.n = len(nums)

        def find_subset(index, current):
            if index == self.n:
                self.ans.append(current[:])
                return
            current.append(nums[index])
            find_subset(index + 1, current)
            current.pop()
            find_subset(index + 1, current)
        find_subset(0, [])
        return self.ans