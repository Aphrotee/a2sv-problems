# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_right = 0
        max_left = 0
        left = 0
        right = n - 1
        max_water = 0

        while left < right:
            if height[left] <= height[right]:
                max_water += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
                left += 1
            else:
                max_water += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
                right -= 1
        return max_water