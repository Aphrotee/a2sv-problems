# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        area = 0
        n = len(height)
        l = 0
        r = n - 1

        while l < r:
            a = min(height[r], height[l]) * (r - l)
            max_area = max(max_area, a)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area