# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0

        l = 0
        r = l
        n = len(nums)
        runningProd = 1
        while r < n:
            runningProd *= nums[r]
            if runningProd < k:
                count += (r - l + 1)
            else:
                while l <= r and runningProd >= k:
                    runningProd /= nums[l]
                    l += 1
                count += (r - l + 1)
            r += 1
        return count