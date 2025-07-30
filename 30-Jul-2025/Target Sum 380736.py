# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        self.n = len(nums)
        self.dp = {}

        def getSum(index, Sum):

            if (index, Sum) in self.dp:
                return self.dp[(index, Sum)]
            if index == self.n:
                if Sum == target:
                    return 1
                return 0
            pos = getSum(index + 1, Sum + nums[index])
            neg = getSum(index + 1, Sum - nums[index])
            self.dp[(index, Sum)] = neg + pos
            return self.dp[(index, Sum)]
        
        return getSum(0, 0)