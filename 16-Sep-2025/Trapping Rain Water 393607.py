# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        rain_water = 0
        max_left = height[l]
        max_right = height[r]

        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                rain_water += (max_left - height[l])
                l += 1
            else:
                max_right = max(max_right, height[r])
                rain_water += (max_right - height[r])
                r -= 1

        return rain_water