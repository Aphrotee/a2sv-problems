# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        

        def backtrack(i, current_subset, targ):
            nonlocal ans
            if targ == 0:
                ans.append(current_subset[:])
                return
            if i == len(candidates) or targ < 0:
                return
            current_subset.append(candidates[i])
            backtrack(i, current_subset, targ - candidates[i])
            current_subset.pop()
            backtrack(i+1, current_subset, targ)
        backtrack(0, [], target)
        return ans