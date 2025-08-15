# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.n = len(nums)

        self.dp = {}

        def dfs(index, total):
            if index == self.n:
                if total == target:
                    self.dp[(index, total)] = 1
                    return 1
                return 0
            
            if (index, total) in self.dp:
                return self.dp[(index, total)]
            self.dp[(index, total)] = (dfs(index + 1, total + nums[index])
                                     + dfs(index + 1, total - nums[index]))
            return self.dp[((index, total))]
        return dfs(0, 0)
