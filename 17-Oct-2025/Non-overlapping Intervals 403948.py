# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prevEnd = float("-inf")
        n = len(intervals)

        for i in range(n):
            start, end = intervals[i]
            if prevEnd <= start:
                prevEnd = end
            else:
                count += 1
                
        return count