# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        ans = 1
        for i in range(2, mini + 1):
            if mini % i == 0 and maxi % i == 0:
                ans = i
        return ans