# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        mask = 0

        for i in range(32):
            mask = 1 << i
            count = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                if (mask & num != 0): count += 1
            if count % 3 == 1: ans |= mask
        if ans >= 2**31:
            ans -= 2**32
        return ans