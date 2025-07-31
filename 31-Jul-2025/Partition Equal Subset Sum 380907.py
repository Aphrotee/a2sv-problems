# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subset = set([0])
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        for num in nums:
            temp = set()
            for s in subset:
                x = s + num
                if x == target:
                    return True
                temp.add(x)
                temp.add(s)
            subset = temp
        return False
    