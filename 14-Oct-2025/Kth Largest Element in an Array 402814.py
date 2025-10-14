# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mini = maxi = nums[0]
        for num in nums:
            mini = min(mini, num)
            maxi = max(maxi, num)
        
        bucket = [0] * (maxi - mini + 1)
        for num in nums:
            bucket[num - mini] += 1
        
        for potential in range(maxi - mini, -1, -1):
            k -= bucket[potential]
            if k <= 0:
                return potential + mini
