# Problem: Largest Rectangle in Histogram (Optional) - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                startH, startI = stack.pop()
                width = i - startI
                area = startH * width
                start = startI
                max_area = max(area, max_area)
            stack.append((h, start))

        if stack:
            for i, (h, s) in enumerate(stack):
                max_area = max(max_area, (n - s) * h)
        return max_area
