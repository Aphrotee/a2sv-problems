# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        k = float("-inf")
        ans = 0
        n = len(intervals)
        for i in range(n):
            
            a, b = intervals[i]
            if a >= k:
                k = b
            else:
                ans += 1
        return ans
            