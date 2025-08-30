# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ballons = 1
        end = points[0]
        n = len(points)
        for i in range(1, n):
            if end[1] >= points[i][0]:
                new_interval = [max(end[0], points[i][0]), min(end[1], points[i][1])]
                end = new_interval
            else:
                end = points[i]
                ballons += 1
        return ballons
