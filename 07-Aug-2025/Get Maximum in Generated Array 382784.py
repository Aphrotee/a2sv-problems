# Problem: Get Maximum in Generated Array - https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        if n <= 1:
            return n
        nums[1] = 1
        max_int = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                j = (i - 1) // 2
                nums[i] = nums[j] + nums[j + 1]
            max_int = max(nums[i], max_int)
        return max_int