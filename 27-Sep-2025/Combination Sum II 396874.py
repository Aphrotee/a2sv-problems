# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(i, current_subset, targ):
            nonlocal ans
            if targ == 0:
                ans.append(current_subset[:])
                return
            if i >= len(candidates) or targ < 0:
                return
            current_subset.append(candidates[i])
            backtrack(i+1, current_subset, targ - candidates[i])
            current_subset.pop()
            to_skip = candidates[i]
            while i < len(candidates) and candidates[i] == to_skip:
                i += 1
            backtrack(i, current_subset, targ)
        backtrack(0, [], target)
        return ans