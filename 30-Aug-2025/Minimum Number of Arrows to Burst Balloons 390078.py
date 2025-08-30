# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        merged = [points[0]]
        n = len(points)
        for i in range(1, n):
            if merged[-1][1] >= points[i][0]:
                new_interval = [max(merged[-1][0], points[i][0]), min(merged[-1][1], points[i][1])]
                merged.pop()
                merged.append(new_interval)
            else:
                merged.append(points[i])
        return len(merged)
