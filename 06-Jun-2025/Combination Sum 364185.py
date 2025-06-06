# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        self.n = len(candidates)

        def combine(combo, index, targ):
            if targ == 0:
                # A solution has been found, add to the output
                out.append(combo)
                return
            elif targ < 0 or index == self.n:
                # A solution is no longer possible from this path, backtrack
                return
            # 
            combine(combo + [candidates[index]], index, targ - candidates[index])
            combine(combo, index + 1, targ)
        combine([], 0, target)
        return out