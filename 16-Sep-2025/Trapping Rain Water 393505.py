# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        rain_water = 0

        for i in range(1, n):
            left[i] = max(height[i - 1], left[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = max(height[i + 1], right[i + 1])
        
        for i in range(n):
            rain_water += max(min(left[i], right[i]) - height[i], 0)
        
        return rain_water