# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0

        l = 0
        r = len(height) - 1

        while l < r:
            water = min(height[l], height[r]) * (r - l)
            most_water = max(most_water, water)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return most_water